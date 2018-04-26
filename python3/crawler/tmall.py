import re
import random
import time
import requests
import uuid

from lxml import etree
from bs4 import BeautifulSoup

from ciq.utils.str_format import (str_to_md5str, format_brand)
from ciq.utils.crawler import (save_industry, save_brand, brand_exists, save_industry_brand,
                             save_goods, save_goods_comments, get_arealabel, get_html_fragment_by_xpath, 
                             get_brand_info_by_baike)
from ciq.utils.logger import Logger
'''
scripts/tmall.py -> 天猫国际
'''

pc_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

phone_headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}

logger = Logger()
msg = 'Crawler: <scripts/tmall.py>' 

def category_list():
    url = 'https://www.tmall.hk/'
    resp = requests.get(url, headers=pc_headers, allow_redirects=False).text
    categorys_xpath = '//div[@class="zebra-hk-nav-pc"]//textarea[@id="J_data"]/text()'
    categorys_text = get_html_fragment_by_xpath(resp, categorys_xpath)[0].strip()
    categorys = []
    for c1 in eval(categorys_text).values():
        if type(c1) == type([]):
            for l_c2 in c1:
                industry_name = l_c2['title']

                if industry_name.find('品牌') != -1 or industry_name.find('国际') != -1 or industry_name.find('分类') != -1 or industry_name.find('收藏') != -1:
                    continue

                categorys.append(
                    {
                        'industry_name': industry_name, 
                        'category_urls': list(map(lambda x: 'https:%s' % x['href'], l_c2['secondNav']))
                    }
                )

        if type(c1) == type({}):
            continue

    return categorys


def brand_list(category_url):
    cat = re.compile(r'cat=(.*?)&').findall(category_url)[0]
    spm = re.compile(r'spm=(.*?)&').findall(category_url)
    q = re.compile(r'q=(.*?)&').findall(category_url)

    url = 'https://list.tmall.hk/ajax/allBrandShowForGaiBan.htm'
    headers = pc_headers
    headers['referer'] = category_url
    params = {
        't':'0', 
        'cat':cat, 
        'sort':'d', 
        'style':'g', 
        'auction_tag':'71682', 
        'from':'tmallhk.list.pc_1_searchbutton', 
        'active':'1', 
        'industryCatId':cat, 
        'tmhkmain':'1', 
        'userIDNum':'', 
        'tracknick':'', 
    }

    if q:
        params['q'] = q[0]
    
    if spm:
        params['spm'] = spm[0]

    resp = requests.get(url, headers=headers, params=params, allow_redirects=False)
    return resp.json()


def first60_goods(category_url, industry_name):
    for brand_dict in brand_list(category_url):
        # process brand info
        brand_name = format_brand(brand_dict['title'])
        brand_obj = brand_exists(brand_name)
        if brand_obj:
            i_b_guid = save_industry_brand(brand_obj.name, brand_obj.desc, brand_obj.img, brand_obj.logo, industry_name)
        else:
            try:
                brand_info_tuple = get_brand_info_by_baike(brand_name)
                i_b_guid = save_industry_brand(brand_name, brand_info_tuple[0], brand_info_tuple[1], brand_info_tuple[1], industry_name)
            except Exception as e:
                logger.record('%s, Line: 99, %s' % (msg, e), lt='ERROR')
                continue

        # process goods list
        url = 'https://list.tmall.hk/search_product.htm{0}'.format(brand_dict['href'].replace('amp;', ''))

        headers = pc_headers
        headers['cookie'] = 'cna=XYGtEtVTJTwCARsRPRqvITFQ; enc=5xcy7xuF73Qc71sfKrO3%2Bk0ru3%2BsJhFmUUFSHnqnR4LtP42UnKc9WSLVUOkAvn92hkpnFx99KKxIQyKRyOc1cQ%3D%3D; _med=dw:2048&dh:1152&pw:2560&ph:1440&ist:0; cq=ccp%3D1; UM_distinctid=16204b20e9634b-00ffb709421be6-3b60450b-240000-16204b20e99154; t=5c7300b77eda4600cacc71d944e10b02; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=1783a9498375fe45f32ee116b6a0da6a; _tb_token_=f6c70ebe3ad63; res=scroll%3A2031*5483-client%3A2031*1056-offset%3A2031*5483-screen%3A2048*1152; pnm_cku822=098%23E1hvD9vUvbpvUpCkvvvvvjiPPFzv1jrRR2cU1jivPmPUAj3bRsMZ1jtUn2qyzjDUR4wCvvBvpvpZRphvChCvvvvPvpvhvvvvvvhCvvXvppvvvvmtvpvIphvvvvvvphCvpmvvvvChXhCvUvvvvhLhphv9vvvvBmXvpmvvvvChEuyCvv3vpvoEy4x3SOyCvvXmp99hV1IEvpCWpRC7v8RzEhHI27zpdiB%2BmB%2B%2BaNoAdcwu4Qtr08g78BBlBR2OHF%2BSBkphQRA1%2B2n7OHbhT2eAnhhAcUmxdX368c6Ofwp4derE8xeYyp%3D%3D; isg=BH9_ApslGR4anR39R6zt4LxIDlPJzNOgmJk5bRFMGy51IJ-iGTRjVv0yZvDeY6t-'
        html_doc = requests.get(url, headers=headers, allow_redirects=False).text

        goods_list_xpath = '//div[@class="product-iWrap"]'
        goods_list = get_html_fragment_by_xpath(html_doc, goods_list_xpath)

        for goods in goods_list:
            goods_str = etree.tostring(goods)
            # process goods info
            goods_href_xpath = '//div[@class="productImg-wrap"]/a/@href'
            goods_href = get_html_fragment_by_xpath(goods_str, goods_href_xpath)[0].replace('//detail.tmall.hk/', 'https://detail.m.tmall.com/')
            goods_img_xpath = '//div[@class="productImg-wrap"]/a/img/@src'
            goods_img = 'https:%s' % get_html_fragment_by_xpath(goods_str, goods_img_xpath)[0]
            goods_price_xpath ='//p[@class="productPrice"]/em/@title'
            goods_price = get_html_fragment_by_xpath(goods_str, goods_price_xpath)[0]
            goods_name_xpath = '//p[@class="productTitle"]/a/@title'
            goods_name = get_html_fragment_by_xpath(goods_str, goods_name_xpath)[0]
            goods_source_xpath= '//p[@class="productPrice"]/i/@class'
            try:
                goods_source = get_arealabel(get_html_fragment_by_xpath(goods_str, goods_source_xpath)[0].split('-')[-1].lower())
            except Exception as e:
                goods_source = '全球'
            goods_ecommerce = '天猫国际'

            pageNo = 0
            headers = phone_headers
            headers['cookie'] = 'UM_distinctid=160907e9f4d26d-0a81abf9d0b59f-5a442916-240800-160907e9f4e2ca; cna=XYGtEtVTJTwCARsRPRqvITFQ; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTeP7jGAmqS3A%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=V32FPkk%2FgPzW&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; uc3=nk2=D8zmomNL5X8invij&id2=WvAwOZEEkKj4&vt3=F8dBz4W%2F8KS5lp53%2Bwo%3D&lg2=W5iHLLyFOGW7aA%3D%3D; tracknick=love%5Cu6DD8%5Cu5B9D2012; _l_g_=Ug%3D%3D; unb=904811042; lgc=love%5Cu6DD8%5Cu5B9D2012; cookie1=UNQ%2B9f1p5pZURJ9Q60CdZcT1I%2BbdFxeL8tmdwN6MQpw%3D; login=true; cookie17=WvAwOZEEkKj4; cookie2=1783a9498375fe45f32ee116b6a0da6a; _nk_=love%5Cu6DD8%5Cu5B9D2012; t=5c7300b77eda4600cacc71d944e10b02; sg=228; csg=efcdf0bd; _tb_token_=f6c70ebe3ad63; ucn=unzbyun; _m_h5_tk=4887d94ce4b863a1f82a365a24254068_1521013219797; _m_h5_tk_enc=8415e104022f51bfa23a6f0608b27ae3; isg=AhAQzz1xfjsOyyLWE3DJ7JEt4V6icfSFY5ymsArh32s-RbDvsunEs2Z3aTpf'
            comment_params = {
                'itemId': re.compile(r'id=(.*?)&').findall(goods_href)[0], 
                'sellerId': re.compile(r'user_id=(.*?)&').findall(goods_href)[0], 
                'order': '3', 
                'pageSize': '10', 
            }
            comment_url = 'https://rate.tmall.com/list_detail_rate.htm'
            while pageNo <= 100:
                comment_params['currentPage'] = pageNo
                resp = requests.get(comment_url, headers=phone_headers, params=comment_params, allow_redirects=False)
                try:
                    comment_list = eval(resp.text.replace('"rateDetail":', '').replace('false', '0').replace('true', '1'))['rateList']
                except Exception as e:
                   continue

                if not comment_list:
                    break

                for comment in comment_list:
                    content = comment['rateContent']
                    comment_time = comment['rateDate']
                    grade = 0
                    zan_count = 0
                    reply_count = 0
                    reply_content = ''
                    user_name = comment['displayUserNick']
                    user_photo = ''
                    is_vip = comment['goldUser'] # 1 vip; -1 not vip
                    register_day = 0
                    menmber_grade = comment['userVipLevel']

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
                    comment_dict['ecommerce'] = goods_ecommerce
                    save_goods_comments(comment_dict)

                time.sleep(2)
                pageNo += 1


def run():
    catetorys = category_list()

    while True:
        category = random.choice(catetorys)
        category_urls = category['category_urls']
        category_url = random.choice(category_urls)
        industry_name = category['industry_name']
        logger.record('%s Request <URL: %s, INDUSTRY: %s>' % (msg, category_url, industry_name, ))
        try:
            first60_goods(category_url, industry_name)
        except Exception as e:
            logger.record('%s, Line: 181, %s' % (msg, e, ), lt='ERROR')
            time.sleep(10)
            continue

        