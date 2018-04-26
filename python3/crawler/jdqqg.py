import re
import random
import time
import requests
import uuid

from lxml import etree
from bs4 import BeautifulSoup

from ciq.utils.str_format import (str_to_md5str, format_brand)
from ciq.utils.crawler import (save_industry, save_brand, brand_exists, save_industry_brand,
                             save_goods, save_goods_comments, get_html_fragment_by_xpath, 
                             get_brand_info_by_baike)
from ciq.utils.logger import Logger
'''
scripts/jdqqg.py -> 京东全球购

设置 utf8mb4_unicode_ci ,可以存储emoji:
create database ciq character set utf8mb4;
ALTER TABLE `ciq`.`base_comment` MODIFY `content` TEXT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
'''

pc_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

phone_headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}

logger = Logger()
msg = 'Crawler: <scripts/jdqqg.py>' 

def category_list():
    url = 'http://www.jd.hk/header/getData.do'
    resp = requests.get(url, headers=pc_headers, allow_redirects=False)
    main_category = resp.json()['mainCategory']
    category_list = []

    for c in main_category:
        category_list += c['mainTextLink']

    return category_list


def brand_list(url):
    html_doc = requests.get(url, headers=pc_headers, allow_redirects=False).text
    my_xpath = '//div[@class="sl-v-list"]/ul[@id="brandsArea"]/li/a/@href'
    brand_list = get_html_fragment_by_xpath(html_doc, my_xpath)

    return brand_list


def first60_goods(category_url, industry_name):
    try:
        category = re.compile(r'cat=(.*?)&').findall(category_url)[0].replace(',', '_').replace('%2C', '_')
    except Exception as e:
        logger.record('%s, Line: 57, %s' % (msg, e), lt='ERROR')
        return

    for brand_url in brand_list(category_url):
        # process brand info
        brand_name = format_brand(brand_url.split('品牌_')[1])
        brand_obj = brand_exists(brand_name)
        if brand_obj:
            i_b_guid = save_industry_brand(brand_obj.name, brand_obj.desc, brand_obj.img, brand_obj.logo, industry_name)
        else:
            try:
                brand_info_tuple = get_brand_info_by_baike(brand_name)
                i_b_guid = save_industry_brand(brand_name, brand_info_tuple[0], brand_info_tuple[1], brand_info_tuple[1], industry_name)
            except Exception as e:
                logger.record('%s, Line: 71, %s' % (msg, e), lt='ERROR')
                continue

        # process goods list
        url = 'http://list.jd.hk{0}'.format(brand_url)
        html_doc = requests.get(url, headers=pc_headers, allow_redirects=False).text
        goods_list_xpath = '//div[@id="plist"]/ul/li'
        goods_list = get_html_fragment_by_xpath(html_doc, goods_list_xpath)

        for goods in goods_list:
            goods_str = etree.tostring(goods)

            # process goods info
            goods_href_xpath = '//div[@class="p-name"]/a/@href'
            goods_href = get_html_fragment_by_xpath(goods_str, goods_href_xpath)[0]
            goods_img_xpath = '//div[@class="p-img"]/a/img/@src'
            goods_img = 'http:%s' % get_html_fragment_by_xpath(goods_str, goods_img_xpath)[0]
            goods_name_xpath = '//div[@class="p-name"]/a/em/text()'
            goods_name = get_html_fragment_by_xpath(goods_str, goods_name_xpath)[0].strip()
            goods_id = goods_href[14:-5]
            try:
                headers = pc_headers
                headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
                headers['Accept-Encoding'] = 'gzip, deflate, br'
                headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
                headers['Cache-Control'] = 'no-cache'
                headers['Connection'] = 'keep-alive'
                headers['Pragma'] = 'no-cache'
                headers['Upgrade-Insecure-Requests'] = '1'
                headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
                headers['Host'] = 'p.3.cn'
                goods_price = requests.get('https://p.3.cn/prices/mgets?skuIds=J_%s&pduid=15141908209681329182749' % goods_id, headers=headers, allow_redirects=False).json()[0]['p']
                headers['Host'] = 'c.3.cn'
                try:
                    goods_source = requests.get('https://c.3.cn/globalBuy?skuId=%s' % goods_id, headers=headers, allow_redirects=False).json()['nationName']
                except Exception as e:
                    goods_source = '京东精选'
            except Exception as e:
                logger.record('%s, Line: 94, %s' % (msg, e), lt='ERROR')
                time.sleep(5)
                continue
            headers = pc_headers
            headers['Host'] = 'club.jd.com'
            headers['Referer'] = 'https://item.jd.hk/%s.html' % goods_id

            pageNo = 0
            while pageNo <= 100:
                try:
                    comment_list = requests.get('https://club.jd.com/productpage/p-%s-s-0-t-1-p-%s.html' % (goods_id, pageNo, ) , headers=headers, allow_redirects=False).json()['comments']
                except Exception as e:
                    logger.record('%s, Line: 102, %s' % (msg, e), lt='ERROR')
                    continue

                if not comment_list:
                    break

                for comment in comment_list:
                    content = comment['content']
                    comment_time = comment['creationTime']
                    grade = comment['score']
                    zan_count = comment['usefulVoteCount']
                    reply_count = comment['replyCount']
                    reply_content = ''
                    user_name = comment['nickname']
                    user_photo = comment['userImage']
                    is_vip = 1 if comment['userLevelName'] == 'PLUS会员' else -1  # 1 vip; -1 not vip
                    register_day = comment['days']
                    menmber_grade = comment['userLevelName']

                    comment_dict = {}
                    comment_dict['content'] = content
                    comment_dict['comment_time'] = comment_time
                    comment_dict['grade'] = grade
                    comment_dict['zan_count'] = zan_count
                    comment_dict['user_name'] = user_name
                    comment_dict['user_photo'] = user_photo
                    comment_dict['is_vip'] = is_vip
                    comment_dict['register_day'] = register_day
                    comment_dict['menmber_grade'] = menmber_grade
                    comment_dict['goods_name'] = '{0}...'.format(goods_name[0:250]) if len(goods_name) > 255 else goods_name
                    comment_dict['goods_img'] = goods_img
                    comment_dict['goods_price'] = goods_price
                    comment_dict['goods_source'] = goods_source
                    comment_dict['i_guid'] = i_b_guid[0]
                    comment_dict['b_guid'] = i_b_guid[1]
                    comment_dict['ecommerce'] = '京东全球购'
                    save_goods_comments(comment_dict)

                time.sleep(2)
                pageNo += 1


def run():
    categorys = category_list()
    while True:
        category = random.choice(categorys)
        category_url = 'http:%s' % category['linkText']
        industry = category['text']
        logger.record('%s Request <URL: %s, INDUSTRY: %s>' % (msg, category_url, industry, ))
        try:
            first60_goods(category_url, industry)
        except Exception as e:
            logger.record('%s, Line: 181, %s' % (msg, e, ), lt='ERROR')
            time.sleep(10)
            continue
