#/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import os
from lxml import etree

def getcontents(html):
    return "//div/span[@class='type-string']/text()"
    xpath=[u'孝感市质量技术监督局',"tr/td/span[@id='FormView1_Label1']//text()",
           u'沈阳市质量技术监督局',
           "//td/div[@id='_ctl0_infocontent']//text()|//td/div[@id='_ctl0_infocontent']/p//text()",
           U'内江市工商行政管理局',"//tr/td[@class='news']//text()",
           u'云南省工商行政管理局',"//tr/td/span/p//text()",
           u'温州市质量技术监督局',"//td/span[@id='Contents']/p//text()",
           u'滨州市质量技术监督局',"//tr/td[@style='line-height:30px; font-size:14px']/div/p//text()",
           u'湖北省来凤县工商行政管理局',"//div[@class='show_con_show']/p//text()",
           u'上饶市质量技术监督局',"//td/div[@class='thridtxt']/p//text()",
           u'西双版纳州质量技术监督局',"//div[@id='content']//text()",
           u'甘肃省质量技术监督局',"//div[@id='content']/p//text()",
           u'罗田县工商行政管理局',"//tr/td[@class='news']//text()",
           u'巴州工商行政管理局',"//div[@id='info_content']//text()",
           u'超标电动自行车泛滥_大楚报料台',"//div[@class='des']//text()",
           ]
    for s in range(0,len(xpath),2):
        if re.search(xpath[s],html.text):
            return xpath[s+1]
            break
    return ''



def getpublish_time(html):
    xpath=[u'湖南省质量技术监督局',"//publishtime/text()",
           u'济南市工商行政管理局',"//div[@class='rq']/text()",
           u'温州市质量技术监督局',"//span[@id='lblsj']/text()",
           u'云南省质量技术监督局',"//div[@id='otherContent']/span[2]/text()",
           u'(赣州)|(九江)市质量技术监督局',"//tr/td[@class='title'][6]/div/text()",
           u'无锡质量技术监督局',"//p[@class='explain']/span[2]/text()",
           u'松原市工商行政管理局',"//span[@class='xiangxi_time']/text()",
           u'朝阳市工商行政管理局',"//span[@id='lDate']/text()",
           u'辽宁省工商行政管理局',"//span[@id='Labeltitle']/text()",
           u'湖北省黄石市质量技术监督局',"//ul[@class='list4']/li[1]/span/text()",
           u'潮州市质量技术监督局',"//div[@class='topic_others']/font[3]/text()",
           u'温州市苍南质量技术监督局',"//span[@id='lblsj']/text()",
           u'长春市工商行政管理局',"//div[@style='margin:10px;text-align: right;font-size:12px;']/text()",
           u'杭州市质量技术监督局高新技术产业开发区（滨江）分局',"//span[@id='LabFillTime']/text()",
           u'老河口市工商行政管理',"//tr/td/p[@align='center']/text()",
           u'深圳市市场监督管理局',"//div/div[@class='biaoti_s']/text()",
           u'晋城市工商行政管理局',"//tr[2]/td[@valign='middle']/text()",
           u'杭州市质量技术监督局',"//tr[1]/td[@align='center']/span/text()",
           u'广东省质量技术监督局',"//div/span[@id='docreltime']/text()",
           u'长治市工商行政管理局',"//tr/td/span[@class='sl_time']/text()",
           u'本溪市工商行政管理局',"//div/span[@id='myDate']/text()",
           ur'武汉市(东湖新技术开发区)|(汉阳区)|(硚口区)|(青山区)工商行政管理局',"//tr[1]/td[@width='301']/text()",
           u'甘肃省兰州市工商行政管理局',"//div/p[@class='text_subtitle']/text()",
           u'罗田县工商行政管理局',"//td[@align='center']/span[@class='style10']/text()",
           u'绵阳市质监局',"//tr/td[@class='nava']/text()",
           u'石首市工商行政管理局',"//div/span[@class='navt1']/text()",
           u'淮北市工商行政管理局',"//td/p[@align='center']/font/text()",
           u'广东省云浮市工商行政管理局',"//td[@align='center']/text()",
           u'南宁市质量技术监督局',"//tr/td[@align='center']/text()",
           u'((吉安)|(萍乡)){1,1}市质量技术监督局',"//td[@class='title']/div/text()",
           u'杨凌农业高新技术产业示范区',"//tr[1]/td[6]/text()",
           u'青岛金质网',"//td/div[@align='right']/text()",
           u'上饶市质量技术监督局',"//tr/td[@class='title']/div/text()",
           u'孝感市质量技术监督局',"//td/span[@id='FormView1_Label6']/text()",
           u'南昌质量信息网',"//td/div[@align='center']/text()",
           u'甘孜州工商行政管理局',"//div[@class='news_content_times']//text()",
           u'河源市质量技术监督局',"//tr/td/p[@align='center']/text()",
           u'西安工商行政管理局',"//td/span[@class='timestyle412189699_4546']/text()",
           u'西藏质量技术监督局',"//td/font/text()",
           u'亳州市工商行政管理局', "//span[@id='info_cata']/../following-sibling::td[1]/text()",
           ]
    for s in range(0,len(xpath),2):
        if re.search(xpath[s],html.text):
            return xpath[s+1]
            break
    return ''

