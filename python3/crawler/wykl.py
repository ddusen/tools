import time
import requests
import uuid

from lxml import etree
from bs4 import BeautifulSoup

from ciq.base.models import (Industry, Brand, IndustryBrand, Comment, )
'''
scripts/wykl.py -> 网易考拉

设置 utf8mb4_unicode_ci ,可以存储emoji:
create database ciq character set utf8mb4;
ALTER TABLE `base_comment` MODIFY `content` TEXT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci; 
'''

pc_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

phone_headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}

def init_db(industry_name):
    industry = Industry.objects.filter(name=industry_name, level=4)
    if not industry.exists():
        Industry(
            name=industry_name,
            level=4,
            parent=None,
        ).save()


def save_industry_brand(brand_name, content, url, industry_name):
    industry = Industry.objects.get(name=industry_name, level=4)
    brand = Brand.objects.filter(name=brand_name)
    if not brand.exists():
        Brand(
            name=brand_name,
            content=content,
            url=url,
        ).save()
        IndustryBrand(
            industry=industry,
            brand=Brand.objects.get(name=brand_name)
        ).save()


def save_goods_info_comments(comment_dict):
    brand = Brand.objects.get(name=comment_dict['goods_brand'])

    comment = Comment.objects.filter(comment_time=comment_dict['comment_time'], 
                                    user_name=comment_dict['user_name'], 
                                    register_day=comment_dict['register_day'], 
                                    goods_name=comment_dict['goods_name']
                                    )

    if not comment.exists():
        Comment(
            content=comment_dict['content'],
            comment_time=comment_dict['comment_time'],
            grade=comment_dict['grade'],
            photos=comment_dict['photos'],
            zan_count=comment_dict['zan_count'],
            reply_count=comment_dict['reply_count'],
            reply_content=comment_dict['reply_content'],
            comment_count=comment_dict['comment_count'],
            favorable_rate=comment_dict['favorable_rate'],
            user_name=comment_dict['user_name'],
            user_photo=comment_dict['user_photo'],
            is_vip=comment_dict['is_vip'],
            register_day=comment_dict['register_day'],
            menmber_grade=comment_dict['menmber_grade'],
            goods_name=comment_dict['goods_name'],
            goods_price=comment_dict['goods_price'],
            goods_source=comment_dict['goods_source'],
            goods_brand=Brand.objects.get(name=comment_dict['goods_brand']),
        ).save()


def get_html_fragment_by_xpath(html_doc, my_xpath):
    soup = BeautifulSoup(html_doc, 'lxml')
    tree = etree.HTML(soup.prettify())
    html_fragment = tree.xpath(my_xpath)

    return html_fragment


def get_all_brand(url):
    html_doc = requests.get(url, headers=pc_headers).text

    my_xpath = '//div[contains(@class,"brands") and contains(@class,"brands-cate") and contains(@class,"all") and contains(@class,"ctag")]/a/@href'

    all_brand = get_html_fragment_by_xpath(html_doc, my_xpath)

    return all_brand


def get_first60_goods_info_and_comment_by_brand(category_url, industry_name):
    all_brand = get_all_brand(category_url)

    for brand_url in all_brand:
        url = 'https://www.kaola.com/{0}'.format(brand_url)

        html_doc = requests.get(url, headers=pc_headers).text
        brand_img_xpath = '//div[@class="m-brand"]/a/img/@data-src'
        brand_img = 'https:{0}'.format(get_html_fragment_by_xpath(html_doc, brand_img_xpath)[0])
        brand_name_xpath = '//div[@class="m-brand"]/div[@class="info"]/p/a/span/text()'
        brand_name = get_html_fragment_by_xpath(html_doc, brand_name_xpath)[0].strip()
        brand_content_xpath = '//div[@class="m-brand"]/div[@class="info"]/div[@class="detail"]/p/text()'
        brand_content = get_html_fragment_by_xpath(html_doc, brand_content_xpath)[0].strip()

        save_industry_brand(brand_name, brand_content, brand_img, industry_name)

        goods_list_xpath = '//div[@class="m-result" and @id="searchresult"]/ul[@class="clearfix" and @id="result"]/li[@class="goods"]/div[contains(@class, "goodswrap") and contains(@class, "promotion")]/div[contains(@class, "desc") and contains(@class, "clearfix")]'
        goods_list = get_html_fragment_by_xpath(html_doc, goods_list_xpath)

        for goods in goods_list:
            goods_str = etree.tostring(goods)

            goods_href_xpath = '//div[@class="titlewrap"]/a/@href'
            goods_href = get_html_fragment_by_xpath(goods_str, goods_href_xpath)[0]
            goods_param_xpath = '//div[@class="titlewrap"]/a/@data-param'
            goods_param = get_html_fragment_by_xpath(goods_str, goods_param_xpath)[0]

            goods_title_xpath = '//div[@class="titlewrap"]/a/@title'
            goods_name = get_html_fragment_by_xpath(goods_str, goods_title_xpath)[0].strip()
            goods_price_xpath = '//p[@class="price"]/span[@class="cur"]/text()'
            goods_price = get_html_fragment_by_xpath(goods_str, goods_price_xpath)[1].strip()
            goods_source_xpath = '//p[contains(@class, "goodsinfo") and contains(@class, "clearfix")]/span/text()'
            goods_source = get_html_fragment_by_xpath(goods_str, goods_source_xpath)[0].strip()

            goods_id_xpath = '//div[@class="titlewrap"]/a/@href'
            goods_id = get_html_fragment_by_xpath(goods_str, goods_id_xpath)[0][9:-5]

            comment_url = 'https://m.kaola.com/wapGoods/commentAjax/comment_list.html'
            headers = phone_headers
            headers['origin'] = 'https://m.kaola.com'
            headers['referer'] = 'https://m.kaola.com{0}?{1}'.format(goods_href, goods_param)

            pageNo = 1
            params = {
                'goodsId': goods_id,
                'pageSize':10,
                'tagType':'0',
                'tagName':'全部',
            }

            while pageNo <= 100:
                time.sleep(1)

                params['pageNo'] = pageNo

                comments = requests.get(comment_url, headers=headers, params=params).json()

                if 200 == comments.get('code'):
                    comment_count = comments['body']['totalCount']
                    favorable_rate = comments['body']['productgrade']
                    comment_list = comments['body']['list']

                    for comment in comment_list:
                        content = comment['commentContent']
                        comment_time = comment['createTime']
                        grade = 0
                        photos = str(comment['imgUrlsFor435'])
                        zan_count = comment['zanCount']
                        reply_count = 0
                        reply_content = ''
                        user_name = comment['accountShow']
                        user_photo = comment['avatarKaola']
                        is_vip = -1  # 1 vip; -1 not vip
                        register_day = comment['userRegisterDay']
                        menmber_grade = 0

                        comment_dict = {}
                        comment_dict['content'] = content
                        comment_dict['comment_time'] = comment_time
                        comment_dict['grade'] = grade
                        comment_dict['photos'] = photos
                        comment_dict['zan_count'] = zan_count
                        comment_dict['reply_count'] = reply_count
                        comment_dict['reply_content'] = reply_content
                        comment_dict['comment_count'] = comment_count
                        comment_dict['favorable_rate'] = favorable_rate
                        comment_dict['user_name'] = user_name
                        comment_dict['user_photo'] = user_photo
                        comment_dict['is_vip'] = is_vip
                        comment_dict['register_day'] = register_day
                        comment_dict['menmber_grade'] = menmber_grade
                        comment_dict['goods_name'] = '{0}...'.format(goods_name[0:250])
                        comment_dict['goods_price'] = goods_price
                        comment_dict['goods_source'] = goods_source
                        comment_dict['goods_brand'] = brand_name

                        save_goods_info_comments(comment_dict)


                pageNo+=1


def run():
	url = 'https://www.kaola.com/category/2620.html?zn=top&amp;zp=category-1-1-1' 
	industry_name = '奶粉'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2631.html?zn=top&amp;zp=category-1-1-2' 
	industry_name = '纸尿裤/拉拉裤'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2621.html?zn=top&amp;zp=category-1-1-3' 
	industry_name = '营养辅食'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2664.html?zn=top&amp;zp=category-1-1-4' 
	industry_name = '宝宝用品'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2665.html?zn=top&amp;zp=category-1-1-5' 
	industry_name = '童装童鞋'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2667.html?zn=top&amp;zp=category-1-1-6' 
	industry_name = '孕妈必备'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/1472.html?zn=top&amp;zp=category-2-1-1' 
	industry_name = '护肤'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/1471.html?zn=top&amp;zp=category-2-1-2' 
	industry_name = '面膜'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/1473.html?zn=top&amp;zp=category-2-1-3' 
	industry_name = '彩妆'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2881.html?zn=top&amp;zp=category-2-1-4' 
	industry_name = '防晒修复'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6166.html?zn=top&amp;zp=category-2-1-5' 
	industry_name = '香水/香氛'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3811.html?zn=top&amp;zp=category-3-1-1' 
	industry_name = '精选大牌'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2909.html?zn=top&amp;zp=category-3-1-2' 
	industry_name = '手表配饰'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2894.html?zn=top&amp;zp=category-3-1-3' 
	industry_name = '女士箱包'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2895.html?zn=top&amp;zp=category-3-1-4' 
	industry_name = '服饰内衣'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3494.html?zn=top&amp;zp=category-3-1-5' 
	industry_name = '男士箱包'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2905.html?zn=top&amp;zp=category-3-1-6' 
	industry_name = '鞋'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/12317.html?zn=top&amp;zp=category-4-1-1' 
	industry_name = '洗护日用'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/12344.html?zn=top&amp;zp=category-4-1-2' 
	industry_name = '女性护理'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2731.html?zn=top&amp;zp=category-4-1-3' 
	industry_name = '其他个护'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/10989.html?zn=top&amp;zp=category-4-1-4' 
	industry_name = '宠物生活'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2734.html?zn=top&amp;zp=category-4-1-5' 
	industry_name = '居家用品'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2732.html?zn=top&amp;zp=category-4-1-6' 
	industry_name = '家装家纺'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2893.html?zn=top&amp;zp=category-5-1-1' 
	industry_name = '营养补充'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/2916.html?zn=top&amp;zp=category-5-1-2' 
	industry_name = '健康养护'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3401.html?zn=top&amp;zp=category-5-1-3' 
	industry_name = '女性必备'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3446.html?zn=top&amp;zp=category-5-1-4' 
	industry_name = '关爱老年'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3438.html?zn=top&amp;zp=category-5-1-5' 
	industry_name = '男性必备'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3013.html?zn=top&amp;zp=category-5-1-6' 
	industry_name = '国际汇'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3692.html?zn=top&amp;zp=category-6-1-1' 
	industry_name = '配饰服饰'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/11778.html?zn=top&amp;zp=category-6-1-2' 
	industry_name = '美妆个护'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3681.html?zn=top&amp;zp=category-6-1-3' 
	industry_name = '日用家居'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3676.html?zn=top&amp;zp=category-6-1-4' 
	industry_name = '电子生活'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3668.html?zn=top&amp;zp=category-6-1-5' 
	industry_name = '母婴专区'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/3691.html?zn=top&amp;zp=category-6-1-6' 
	industry_name = '美食保健'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6782.html?zn=top&amp;zp=category-7-1-1' 
	industry_name = '手机/配件'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6810.html?zn=top&amp;zp=category-7-1-2' 
	industry_name = '数码影音'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6866.html?zn=top&amp;zp=category-7-1-3' 
	industry_name = '生活电器'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6839.html?zn=top&amp;zp=category-7-1-4' 
	industry_name = '个护健康'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6826.html?zn=top&amp;zp=category-7-1-5' 
	industry_name = '厨房电器'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6867.html?zn=top&amp;zp=category-7-1-6' 
	industry_name = '办公/外设'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/5864.html?zn=top&amp;zp=category-8-1-1' 
	industry_name = '乳品/咖啡/麦片/冲饮'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/5924.html?zn=top&amp;zp=category-8-1-2' 
	industry_name = '人气热门'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/5882.html?zn=top&amp;zp=category-8-1-3' 
	industry_name = '茶/酒/饮料'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/6088.html?zn=top&amp;zp=category-8-1-4' 
	industry_name = '粮油副食'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/5913.html?zn=top&amp;zp=category-8-1-5' 
	industry_name = '休闲零食'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/5905.html?zn=top&amp;zp=category-8-1-6' 
	industry_name = '饼干糕点'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9694.html?zn=top&amp;zp=category-9-1-1' 
	industry_name = '运动鞋'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9695.html?zn=top&amp;zp=category-9-1-2' 
	industry_name = '运动服装'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9696.html?zn=top&amp;zp=category-9-1-3' 
	industry_name = '户外鞋靴'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9697.html?zn=top&amp;zp=category-9-1-4' 
	industry_name = '户外服装'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9698.html?zn=top&amp;zp=category-9-1-5' 
	industry_name = '户外装备'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9859.html?zn=top&amp;zp=category-9-1-6' 
	industry_name = '更多分类'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9611.html?zn=top&amp;zp=category-10-1-1' 
	industry_name = '新鲜水果'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9612.html?zn=top&amp;zp=category-10-1-2' 
	industry_name = '肉品禽蛋'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9613.html?zn=top&amp;zp=category-10-1-3' 
	industry_name = '水产海鲜'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

	url = 'https://www.kaola.com/category/9614.html?zn=top&amp;zp=category-10-1-4' 
	industry_name = '速冻特产'
	print('EXCUTE < industry_name:{0}, url:{1} >'.format(industry_name, url))
	init_db(industry_name)
	get_first60_goods_info_and_comment_by_brand(url, industry_name)

