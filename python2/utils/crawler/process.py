#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/sdu/Project/tools/code/utils/date')
import cgi
import datetime
import re
import time
import urllib
import urlparse
import random
import socket
import chardet
import requests

from bs4 import BeautifulSoup
from lxml import etree
from lxml import html as html2
from datetime import datetime as datetime2
from convert import datetime_to_timestamp


def extract_link_by_xpath(tree, xpath_link, current_url=''):
    url_list = tree.xpath(xpath_link)
    return [join_path(current_url, url.strip()) for url in url_list]


def extract_pubtime_by_xpath(tree, xpath_pubtime):
    pubtime_list = tree.xpath(xpath_pubtime)
    return [datetime_to_timestamp(for_time(pubtime.xpath("string()"))) for pubtime in pubtime_list]


def extract_item_by_xpath(html_doc, xpath_item):
    soup = BeautifulSoup(html_doc, 'lxml')
    tree = etree.HTML(soup.prettify())
    return tree.xpath(xpath_item)


def get_max_page_number(text, re_page_number):
    page_number_list = re.findall(re_page_number, text)
    page_number_list_len = len(page_number_list)
    if page_number_list_len < 1:
        return 0
    elif page_number_list_len == 1:
        return page_number_list[0]
    else:
        return page_number_list[page_number_list_len - 1]


def extract_item_by_re(text, re_item):
    return re.findall(re_item, text)


def extract_link_by_re(text, re_link, current_url=''):
    temp_link_list = re.findall(re_link, text)
    link_list = []
    if current_url == "":
        return temp_link_list
    else:
        for temp_link in temp_link_list:
            temp_link = join_path(current_url, temp_link.strip())
            link_list.append(temp_link)
        return link_list


def extract_pubtime_by_re(text, re_pubtime):
    temp_pubtime_list = re.findall(re_pubtime, text)
    pubtime_list = []
    for temp_pubtime in temp_pubtime_list:
        pubtime = ''

        dt = datetime2.strptime(temp_pubtime, '%Y-%m-%d')
        pubtime = datetime_to_timestamp(dt)
        pubtime_list.append(pubtime)
    return pubtime_list


def is_last_node(pubtime, last_pubtime):
    if last_pubtime is not None and last_pubtime >= pubtime:
        return True

    return False


def extract_title_by_xpath(tree, xpath_title):
    title_list = tree.xpath(xpath_title)
    if len(title_list) > 0:
        title = title_list[0].xpath("string(.)").strip()
        return title
    return ""


def extract_content_tree_by_xpath(tree, current_url, content_url):
    url_list = tree.xpath(content_url)
    if url_list:
        url = join_path(current_url, url_list[0].strip())
        response = get_response(url)
        return etree.HTML(response.text)
    return None


def extract_content_by_xpath(tree, url, xpath_content, content_url=''):
    if content_url:
        content_tree = extract_content_tree_by_xpath(tree, url, content_url)
        content_list = content_tree.xpath(xpath_content)
    else:
        content_list = tree.xpath(xpath_content)
    if len(content_list) > 0:
        content_all = html2.tostring(content_list[0], encoding=unicode)
        content_text = content_list[0].xpath("string(.)").strip()
        content_all = clear_label(content_all, url)
        content_text = clear_space(content_text)
        return {
            "content_all": content_all,
            "content_text": content_text,
        }
    else:
        return {
            "content_all": "",
            "content_text": "",
        }


def convert_escape(text):
    match = re.findall(r"%u(\w{4})", text)
    sp_list = re.split(r"%u\w{4}", text)
    new_text = ""
    for i in range(len(match)):
        new_text += sp_list[i] + unichr(int(match[i], 16))
    return new_text


def extract_html(text):
    re_str = re.compile(r"<html>.*</html>", re.S)
    match = re.search(re_str, text)
    return match.group(0)


def extract_xml(text):
    re_str = re.compile(r"<\?xml.*</xml>", re.S)
    match = re.search(re_str, text)
    return match.group(0)


def _findstr(text, count=1):
    index = 0
    for i in range(0, count):
        if not index:
            index = text.rfind("/")
        else:
            index = text[:index].rfind("/")
    return index


def for_time(old_time):
    old_time = old_time.strip()
    # old_time == ''
    if not old_time:
        return None
    old_time = old_time.replace(u"年", " ").replace(
        u"月", " ").replace(u"日", " ")
    # match include "2015-11-25 10:10:10", "2015/11/25 10:10:10","2015 11 25
    # 10:10:10", "2015\11\25 10:10:10"
    match = re.search(
        "\d{4}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}\D*?\d{1,2}:\d{1,2}:\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%Y" + match.group(1) + "%m" + match.group(2) + "%d" +
                                          " " + "%H" + ":" + "%M" + ":" + "%S")
    # match include "2015-11-25 10:10", "2015/11/25 10:10","2015 11 25 10:10",
    # "2015\11\25 10:10"
    match = re.search(
        "\d{4}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}\D*?\d{1,2}:\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%Y" + match.group(1) + "%m" + match.group(2) + "%d" +
                                          " " + "%H" + ":" + "%M")
    # match include "10:10:10 2015-11-25", "10:10:10 2015/11/25","10:10:10
    # 2015 11 25", "10:10:10 2015\11\25"
    match = re.search(
        "\d{1,2}:\d{1,2}:\d{1,2}\D*?\d{4}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%H" + ":" + "%M" + ":" + "%S" + " " + "%Y" + match.group(1) +
                                          "%m" + match.group(2) + "%d")
    # match include "10:10 2015-11-25", "10:10 2015/11/25","10:10 2015 11 25",
    # "10:10 2015\11\25"
    match = re.search(
        "\d{1,2}:\d{1,2}\D*?\d{4}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%H" + ":" + "%M" + " " + "%Y" + match.group(1) +
                                          "%m" + match.group(2) + "%d")
    # match include "10:10:10 25-11-2015", "10:10:10 25-11-2015","10:10:10
    # 25-11-2015", "10:10:10 25-11-2015"
    match = re.search(
        "\d{1,2}:\d{1,2}:\d{1,2}\D*?\d{1,2}([-\/ ])+?\d{1,2}([-\/ ])+?\d{4}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%S" + ":" + "%M" + ":" + "%H" + " " + "%d" + match.group(1) +
                                          "%m" + match.group(2) + "%Y")
    # match include "10:10 25-11-2015", "10:10 25-11-2015","10:10 25-11-2015",
    # "10:10 25-11-2015"
    match = re.search(
        "\d{1,2}:\d{1,2}\D*?\d{1,2}([-\/ ])+?\d{1,2}([-\/ ])+?\d{4}", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%M" + ":" + "%H" + " " + "%d" + match.group(1) +
                                          "%m" + match.group(2) + "%Y")
    # match include "2015-11-25", "2015/11/25","2015 11 25", "2015\11\25"
    match = re.search("(\d{4})([-\/ ])(\d{1,2})([-\/ ])(\d{1,2})", old_time)
    if match:
        return datetime.datetime.strptime(match.group(0), "%Y" + match.group(2) + "%m" + match.group(4) + "%d")
    # match include "10天前"
    match = re.search(u"(\d+?)天前", old_time)
    if match:
        return datetime.datetime.now() - datetime.timedelta(days=int(match.group(1)))
    # match include "10小时前", "10时前", "10钟头前", "10个小时前", "10个时前", "10个钟头前"
    match = re.search(u"(\d+?)(小时前|时前|钟头前|个小时前|个时前|个钟头前)", old_time)
    if match:
        return datetime.datetime.now() - datetime.timedelta(hours=int(match.group(1)))
    # match include "10分钟前", "10分前"
    match = re.search(u"(\d+?)(分钟前|分前)", old_time)
    if match:
        return datetime.datetime.now() - datetime.timedelta(minutes=int(match.group(1)))
    # match include "10秒前"
    match = re.search(u"(\d+?)秒前", old_time)
    if match:
        return datetime.datetime.now() - datetime.timedelta(seconds=int(match.group(1)))
    # match include "15-11-25", "15/11/25","15 11 25", "15年11月25日"
    match = re.search("\d{2}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime("20" + match.group(0), "%Y" + match.group(1) + "%m" + match.group(2) + "%d")
    return None
    # match include "15-11-25 10:10:10", "15/11/25 10:10:10","15 11 25
    # 10:10:10", "15年11月25日 10:10:10"
    match = re.search(
        "\d{2}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}\D*?\d{1,2}:\d{1,2}:\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime("20" + match.group(0), "%Y" + match.group(1) + "%m" + match.group(2) + "%d" +
                                          " " + "%H" + ":" + "%M" + ":" + "%S")
    # match include "15-11-25 10:10", "15/11/25 10:10","15 11 25 10:10",
    # "15年11月25日 10:10"
    match = re.search(
        "\d{2}([-\/ ])+?\d{1,2}([-\/ ])+?\d{1,2}\D*?\d{1,2}:\d{1,2}", old_time)
    if match:
        return datetime.datetime.strptime("20" + match.group(0), "%Y" + match.group(1) + "%m" + match.group(2) + "%d" +
                                          " " + "%H" + ":" + "%M")
    return None


def get_web_data(url, data={}, params={}, headers={}, allow_redirects=True):
    count = 0
    html_stream = None
    while count < 2:
        try:
            if data:
                html_stream = requests.post(
                    url, timeout=5, data=data, headers=headers, allow_redirects=allow_redirects)
            else:
                if params:
                    html_stream = requests.get(
                        url, params=params, timeout=5, headers=headers, allow_redirects=allow_redirects)
                else:
                    html_stream = requests.get(
                        url, timeout=5, headers=headers, allow_redirects=allow_redirects)

        except requests.exceptions.Timeout:
            if count == 1:
                raise Exception("requests %s timeout!" % url)
            time.sleep(random.randint(1, 5))

        except socket.timeout:
            if count == 1:
                raise Exception("socket %s timeout!" % url)
            time.sleep(random.randint(1, 8))

        except Exception:
            raise Exception("requests %s fail!" % url)

        else:
            break

        finally:
            count += 1

    return html_stream


def get_response(url, encoding='', data={}, params={}, headers={}, allow_redirects=True):
    response = get_web_data(url, data=data, params=params, headers=headers,
                            allow_redirects=allow_redirects)
    if encoding == '':
        response.encoding = get_charset(response)
    else:
        response.encoding = encoding

    return response


def join_path(url, end_url):
    new_url = ""
    # url =  http(s)://demo1/demo2/demo3
    # ../demo.jpg => http(s)://demo1/demo2/demo.jpg
    if end_url.startswith("../"):
        count = end_url.count("../")
        index = _findstr(url, count=count + 1)
        url = url[:index + 1]
        if not re.search("://", url):
            return ""
        end_url = re.findall("../" * count + "(.*)", end_url)[0]
        new_url = url + end_url
    # /demo.jpg => http(s)://demo1/demo,jpg
    elif end_url.startswith("/"):
        if url.startswith("http"):
            urls = url.split("://")
            root = urls[0] + "://" + \
                re.match("(?<=).*?(?=/)", urls[1]).group(0)
            new_url = root + end_url
    elif end_url.startswith("./"):
        temp_url = ""
        parts = url.split("/")
        for i in range(len(parts) - 1):
            temp_url += parts[i] + "/"
        new_url = temp_url + end_url.replace("./", "")
    # http(s)://demo1/demo2/demo3/demo.jpg => just return self
    elif end_url.startswith("http"):
        return end_url
    else:
        temp_url = ""
        parts = url.split("/")
        for i in range(len(parts) - 1):
            temp_url += parts[i] + "/"
        if temp_url.endswith("/"):
            new_url = temp_url + end_url
        else:
            new_url = temp_url + "/" + end_url
    return new_url


def _wrap(lit):
    if isinstance(lit, list):
        return list(lit)
    else:
        return None


def new_time():
    lo_time = time.time()
    crtimes = {
        "crtime_int": int(lo_time * 1000000),
        "crtime": datetime.datetime.utcfromtimestamp(lo_time),
    }
    return crtimes


def local2utc(local_st):
    assert isinstance(local_st, datetime.datetime)
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st


def get_code(url):
    codes = {}
    count = 0
    parts = urlparse.urlsplit(url)
    parts = parts._replace(path=urllib.quote(parts.path.encode('utf8')))
    url = parts.geturl()
    while count < 2:
        try:
            data = urllib.urlopen(url).read()
            codes = chardet.detect(data)
        except IOError:
            count += 1
        else:
            break
    return codes


def get_charset(html):
    try:
        soup = BeautifulSoup(html[html.find(">") + 1:], "lxml")
    except:
        return 'utf-8'
    tags = soup.find_all(re.compile(r'meta', re.I))
    for tag in tags:
        if tag.get('content'):
            match = re.search(r'charset=(.*)', tag['content'])
            if match:
                coding = match.group(1)
                return coding
    return 'utf-8'


def extract_url(text):
    if not text:
        return ""
    if not isinstance(text, unicode):
        text = unicode(text, 'utf8')

    chinese_symbols = u"[“”‘’！？—…。，·：、￥（）【】《》〖〗]"
    en_symbols = r"[`~!@#\$%\^&\*\(\)_\+=\-\{\}\[\];:\",\.<>/\?\\|' + \"\']"
    text = re.sub(chinese_symbols, ' ', text)
    text = re.sub(en_symbols, ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip().lower()


def clear_space(text):
    text = unicode(text) if type(text) == str else text
    assert isinstance(text, unicode)
    text = re.sub(r'\s+', '', text)
    text = text.replace(' ', '')
    text = text.replace(ur'　', '')
    text = text.replace(ur' ', '')
    return text


def clear_a(text):
    assert isinstance(text, list)
    content = ''
    for item in text:
        item = unicode(item)
        str_comp = r"<a.+?</a>|<script.+?</script>|(?<=class=\").+?(?=\")|(?<=id=\").+?(?=\")"
        strinfo = re.compile(str_comp, re.DOTALL)
        item = strinfo.sub('', item)
        symbols = re.compile(ur'\s+｜')
        item = symbols.sub('', item)
        str_p = re.compile(r"<p.*?>\s+?</p>|<span .+?>\s+?</span>")
        item = str_p.sub('', item)
        content += item.strip()
    return content


def clear_label(text, root):
    if not isinstance(text, unicode):
        text = unicode(text)
    text = text.strip()
    cins_str = r"(class=[\'\"].*?[\"\']|id=[\'\"].*?[\"\']|name=[\'\"].*?[\"\']"\
        "|<!—.*?—>|<a.*?javascript.*?>|<script.*?script>|<\?xml.*?>|(?<=>).*?(?=\S))"
    cins_re = re.compile(cins_str, re.S)
    text = re.sub(cins_re, '', text)
    # current the url of images
    if root:
        link_re = r"href=[\'\"](.*?)[\'\"]|src=[\'\"](.*?)[\'\"]|background=[\'\"](.*?)[\'\"]"
        link_list = re.findall(link_re, text)
        for link_tuple in link_list:
            for link in link_tuple:
                if link:
                    new_link = join_path(root, link)
                    text = text.replace(link, new_link)

    return text


class HandleContent(object):

    def __init__(self):
        pass

    @staticmethod
    def get_BScontext(html, text=False):
        try:
            soup = BeautifulSoup(html, "lxml") if text else BeautifulSoup(
                html.text, "lxml")
        except:
            soup = ''
        return soup

    @staticmethod
    def get_item(html, xpath=''):
        tree = etree.HTML(html.text)
        dom = tree.xpath(xpath)
        return dom

    @staticmethod
    def get_context(html, xpath, text=False):
        texts = ''
        tree = html if text else etree.HTML(html.text)
        dom = tree.xpath(xpath)
        for item in dom:
            if item.strip() == '':
                continue
            else:
                texts += item.strip() if text else ' ' + item.strip()
        return texts.strip()

    @staticmethod
    def get_author(html, xpath='', xp_text=u'作者：', STR=False):
        text = html if STR else HandleContent.get_context(html, xpath)
        author = re.search(u'%s([\u4e00-\u9fa5]+)' % xp_text, text)
        lam_aut = lambda x: x.group(1) if x else ''
        author = lam_aut(author)
        return author

    @staticmethod
    def get_title(html, xpath=''):
        title = HandleContent.get_context(html, xpath)
        if title.strip() == '':
            soup = HandleContent.get_BScontext(html)
            title = soup.title.text.strip() if soup.title else ''

        return title

    @staticmethod
    def strformat(time_str):
        time_str = time_str.strip()
        time_format = ''
        if time_str.find('/') > 0:
            if time_str.find(':') > 0:
                time_format = "%Y/%m/%d %H:%M:%S"
            else:
                time_format = "%Y/%m/%d"
        elif time_str.find(':') == -1:
            time_format = "%Y-%m-%d"
        elif time_str.count(':') == 1:
            time_format = "%Y-%m-%d %H:%M"
        else:
            time_format = "%Y-%m-%d %H:%M:%S"
        try:
            pub_time = datetime.datetime.strptime(time_str, time_format)
        except:
            pub_time = ''
        return datetime_to_timestamp(pub_time)

    @staticmethod
    def get_pubtime(html, xpath='', time_format='', match_str=''):
        text = HandleContent.get_context(html, xpath)
        if text.strip() == '':
            pub_time = HandleContent.find_pubtime(html.text)
        elif match_str:
            match = re.search(match_str, text)
            date_format = time_format if time_format else HandleContent.get_time_format(
                match)
            pub_time = datetime.datetime.strptime(text, date_format)
        else:
            pub_time = HandleContent.find_pubtime(text)
        pub_time = local2utc(
            pub_time) if pub_time else datetime.datetime.utcfromtimestamp(0)
        nowyear = datetime.datetime.now().year
        pubyear = pub_time.year
        if pubyear > nowyear:
            pub_time = pub_time.replace(nowyear)
        return pub_time

    @staticmethod
    def find_pubtime(text):
        return for_time(text)


class HandleUrl(object):

    def __init__(self):
        pass

    @staticmethod
    def join_url_path(root, path):
        path = path.strip()
        path.replace('', '.')
        ls = root.split('/')
        root = ls[0] + '//' + ls[1] + ls[2]
        match = re.search(r'.*?(\w.+$)', path)
        if match:
            path = match.group(1)
        return root + '/' + path

    @staticmethod
    def get_url(data):
        link_list = re.findall(
            r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
        return _wrap(link_list)

    # @staticmethod
    # def judge_url(text, )

    @staticmethod
    def judge_url(url, homepage):
        url_res = ''
        if re.search('(ist)|(.doc)|(.rar)|(.css)|(;)|(\')|(\")', url) or url[-1] in ['/', '#', '=']:
            return url_res
        elif url.find('javascript') >= 0:
            return url_res
        elif url.find('http') == -1:
            url_res = HandleUrl.join_url_path(homepage, url)
        else:
            ls = homepage.split('/')
            root = ls[0] + '//' + ls[1] + ls[2]
            if url.find(root) >= 0 and url[0:4] == 'http':
                url_res = url.strip()
        return url_res
