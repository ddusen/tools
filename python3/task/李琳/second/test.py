# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
#网站域名
head = 'http://www.bjtsb.gov.cn/'

#头信息
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

#网址
begin_url = 'http://www.bjtsb.gov.cn/index.asp?KindID=1422'

num=0

def get_url(url,num):
    num=num+1
    
    #打开一个页面
    page=requests.get(url=url,headers=header)
    page.encoding = 'gbk'
    text=page.text
    soup=BeautifulSoup(text,'html.parser')
    #找到所有的class为td-dotline的td标签
    td=soup.find_all('td',class_='td-dotline')
    # for item in td:
    #   print item.a
    #遍历每一个td里面的a标签
    for i in range(len(td)):
        # 取每一个td里面的a标签
        a=td[i].a
        print (a.string)
        #print a.string
        print (head+a['href'])
        time=td[i]
        b=str(time)
        print (re.findall(r'（(....-..-..)）', b)[0])
       
    
    
        
#拼接每一个下一页
    if num<=13:
        url_next='http://www.bjtsb.gov.cn/index.asp?page='+str(num)+'&KindID=1422&LKindID=0&ClassID=0'
        get_url(url_next,num)
      

    
get_url(begin_url,num)





