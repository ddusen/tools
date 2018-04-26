import uuid
import time
import random
import requests

from lxml import etree
from bs4 import BeautifulSoup

from ciq.utils.crawler import (save_industry, save_brand, save_industry_brand, save_goods, save_goods_comments, get_html_fragment_by_xpath, )
from ciq.utils.str_format import (str_to_md5str, format_brand, )
from ciq.utils.logger import Logger
'''
scripts/wykl.py -> 网易考拉

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
msg = 'Crawler: <scripts/wykl.py>' 


def category_list():
    url = 'https://www.kaola.com/getFrontCategory.shtml'
    resp = requests.get(url, headers=pc_headers, allow_redirects=False)
    main_category = resp.json()

    categorys = []
    for x in main_category['frontCategoryList']:
        for y in x['childrenNodeList']:
            categorys.append({'industry_name': y['categoryName'], 
                    'category_url': 'https://www.kaola.com/category/%s.html' % y['categoryId'], 
                    })
    return categorys


def get_all_brand(url):
    html_doc = requests.get(url, headers=pc_headers, allow_redirects=False).text

    my_xpath = '//div[contains(@class,"brands") and contains(@class,"brands-cate") and contains(@class,"all") and contains(@class,"ctag")]/a/@href'

    all_brand = get_html_fragment_by_xpath(html_doc, my_xpath)

    return all_brand

def get_brand_img(req_url):
    html_doc = requests.get(req_url, headers=pc_headers, allow_redirects=False).text
    my_xpath = '//div[@class="m-brand2"]/img/@src'
    brand_imgs = get_html_fragment_by_xpath(html_doc, my_xpath)
    try:
        brand_img = 'https:{0}'.format(brand_imgs[0])
    except Exception as e:
        logger.record('%s, %s', (msg, e, ), lt='ERROR')
        brand_img = 'https://www.jordans.com/~/media/jordans%20redesign/no-image-found.ashx?h=275&la=en&w=275&hash=F87BC23F17E37D57E2A0B1CC6E2E3EEE312AAD5B'
    return brand_img


def get_first60_goods_info_and_comment_by_brand(category_url, industry_name):
    all_brand = get_all_brand(category_url)

    for brand_url in all_brand:
        url = 'https://www.kaola.com/{0}'.format(brand_url)

        html_doc = requests.get(url, headers=pc_headers, allow_redirects=False).text
        brand_logo_xpath = '//div[@class="m-brand"]/a/img/@data-src'
        brand_img_xpath = '//div[@class="m-brand"]/a/@href'
        
        try:
            brand_img_url = get_html_fragment_by_xpath(html_doc, brand_img_xpath)
            brand_img = get_brand_img('https://www.kaola.com{0}'.format(brand_img_url[0]))
            brand_logo = 'https:{0}'.format(get_html_fragment_by_xpath(html_doc, brand_logo_xpath)[0])
        except Exception as e:
            logger.record('%s, %s', (msg, e, ), lt='ERROR')
            brand_logo = 'https://www.jordans.com/~/media/jordans%20redesign/no-image-found.ashx?h=275&la=en&w=275&hash=F87BC23F17E37D57E2A0B1CC6E2E3EEE312AAD5B'
            brand_img = brand_logo

        brand_name_xpath = '//div[@class="m-brand"]/div[@class="info"]/p/a/span/text()'
        brand_name = get_html_fragment_by_xpath(html_doc, brand_name_xpath)[0].strip()
        brand_desc_xpath = '//div[@class="m-brand"]/div[@class="info"]/div[@class="detail"]/p/text()'
        brand_desc = get_html_fragment_by_xpath(html_doc, brand_desc_xpath)[0].strip()

        i_b_guid = save_industry_brand(format_brand(brand_name), brand_desc, brand_img, brand_logo, industry_name)

        goods_list_xpath = '//div[@class="m-result" and @id="searchresult"]/ul[@class="clearfix" and @id="result"]/li[@class="goods"]/div[contains(@class, "goodswrap") and contains(@class, "promotion")]'
        goods_list = get_html_fragment_by_xpath(html_doc, goods_list_xpath)

        for goods in goods_list:
            goods_str = etree.tostring(goods)
             
            goods_img_xpath = '//div[contains(@class, "goodswrap") and contains(@class, "promotion")]/a/div[@class="img"]/img/@data-src'
            goods_img = 'http:%s' % get_html_fragment_by_xpath(goods_str, goods_img_xpath)[0]
            goods_href_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/div[@class="titlewrap"]/a/@href'
            goods_href = get_html_fragment_by_xpath(goods_str, goods_href_xpath)[0]
            goods_param_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/div[@class="titlewrap"]/a/@data-param'
            goods_param = get_html_fragment_by_xpath(goods_str, goods_param_xpath)[0]

            goods_title_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/div[@class="titlewrap"]/a/@title'
            goods_name = get_html_fragment_by_xpath(goods_str, goods_title_xpath)[0].strip()
            goods_price_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/p[@class="price"]/span[@class="cur"]/text()'
            goods_price = get_html_fragment_by_xpath(goods_str, goods_price_xpath)[1].strip()
            goods_source_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/p[contains(@class, "goodsinfo") and contains(@class, "clearfix")]/span/text()'
            goods_source = get_html_fragment_by_xpath(goods_str, goods_source_xpath)[0].strip()

            goods_id_xpath = '//div[contains(@class, "desc") and contains(@class, "clearfix")]/div[@class="titlewrap"]/a/@href'
            goods_id = get_html_fragment_by_xpath(goods_str, goods_id_xpath)[0][9:-5]

            comment_url = 'https://m.kaola.com/wapGoods/commentAjax/comment_list.html'
            headers = phone_headers
            headers['origin'] = 'https://m.kaola.com'
            headers['referer'] = 'https://m.kaola.com{0}?{1}'.format(goods_href, goods_param)

            pageNo = 1
            params = {
                'goodsId': goods_id,
                'pageSize': 10,
                'tagType': '0',
                'tagName': '全部',
            }

            while pageNo <= 100:
                time.sleep(1)

                params['pageNo'] = pageNo

                try:
                    comments = requests.get(comment_url, headers=headers, params=params, allow_redirects=False).json()
                except Exception as e:
                    logger.record('%s, %s', (msg, e, ), lt='ERROR')
                    continue

                if 200 == comments.get('code'):
                    comment_list = comments['body']['list']

                    if not comment_list:
                        break

                    for comment in comment_list:
                        content = comment['commentContent']
                        comment_time = comment['createTime']
                        grade = 0
                        zan_count = comment['zanCount']
                        reply_count = 0
                        reply_content = ''
                        user_name = comment['accountShow']
                        user_photo = comment['avatarKaola']
                        is_vip = -1  # 1 vip; -1 not vip
                        register_day = comment['userRegisterDay']
                        menmber_grade = ''

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
                        comment_dict['ecommerce'] = '网易考拉海购'
                        save_goods_comments(comment_dict)

                pageNo += 1


def run():
    categorys = category_list()
    while True:
        category = random.choice(categorys)
        category_url = category['category_url']
        industry_name = category['industry_name']
        logger.record('%s Request <URL: %s, INDUSTRY: %s>' % (msg, category_url, industry_name, ))
        try:
            save_industry(industry_name)
            get_first60_goods_info_and_comment_by_brand(category_url, industry_name)
        except Exception as e:
            logger.record('%s, Line: 181, %s' % (msg, e, ), lt='ERROR')
            time.sleep(10)
            continue
