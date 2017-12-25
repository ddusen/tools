# coding=utf-8
import requests
from bs4 import BeautifulSoup
import MySQLdb
import re
connection =MySQLdb.connect(
    host="localhost",
    user="root",
    passwd ="123456",
    port=3306,
    db="tt",
    charset="utf8mb4",
)

#获取游标
cursor = connection.cursor()

#创建SQL语句
sql_insert ="insert into `aa` (`title`,`url`,`pubtime`)\
            values(%s,%s,%s)"

sql_select = "select url from aa"


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
        print a.string
        #print a.string
        print head+a['href']
        time=td[i]  
        #print str(time)[-18:-8]
        b=str(time)
        print re.findall(r'（(....-..-..)）', b)[0]

    
        #将要写入数据库的记录先存入values
        # print a.string ,type(a.string)
        # print a.string.encode('utf-8')
        # print type(a.string.encode('utf-8'))
        # i = 10 /0
        a1 = a.string.encode('utf-8')
        a2 = (head+a['href']).encode('utf-8')
        a3 = re.findall(r'（(....-..-..)）', b)[0]
        values = (a1, a2, a3)
        # print values
        #执行MySQL语句，写入数据库
        cursor.execute(sql_insert,values)

    
        
#拼接每一个下一页
    if num<=13:
        url_next='http://www.bjtsb.gov.cn/index.asp?page='+str(num)+'&KindID=1422&LKindID=0&ClassID=0'
        get_url(url_next,num)



#get_url(begin_url,num)
cursor.execute(sql_select)

url_all=cursor.fetchall()



def get_url1(url_all):
    # 打开一个页面

    for i in range(len(url_all)): 

        #print url
        page=requests.get(list(url_all[i])[0])
        #page = requests.get(url=url, headers=header)
        page.encoding = 'gbk'
        text=page.text
        soup=BeautifulSoup(text,'html.parser')
       
        
        
        #标题
        div=soup.find('div',class_='article-title')
        p_title = div.get_text()
        #print p_title

        #时间
        td_time=soup.find('td',class_='grey-bg')
        pubtime=str(td_time)[-15:-5]
        #print pubtime

        #发布者
        
        div_content =soup.find('div',class_='font12')
        print div_content.get_text()
        p = div_content.find('p',align='right')
        try:
            author = p.get_text()[:10]
            #print author
        except:
            print 'none' 


        #获取内容所在div的所有p标签

        p_content=div_content.find_all('p')
        p_article=''
    
        for i in p_content:
            #print i.attrs
            
            #判断不属于文章内容的p标签
            if i.attrs =={'align': 'right'} or i.attrs== {'align': 'center'} or i.attrs== {'align': 'left'}:
                break
            else:
            #将所有属于内容的p标签的内容相加
                p_article +=i.get_text()
                #print p_article
        print p_title,'\n',pubtime,'\n',author,'\n',p_article
        #创建sql语句 
        sql_insert1=u"INSERT INTO bb VALUES(%s,%s,%s,%s)"
        values=(p_title,pubtime,author,p_article)
        cursor.execute(sql_insert1,values) 
 

        
get_url1(url_all)  

#print values


 
#关闭游标
cursor.close()
#提交
connection.commit()
#关闭连接
connection.close()
