# coding:utf-8
import requests
from bs4 import BeautifulSoup
import MySQLdb

#连接数据库
db = MySQLdb.connect('localhost','root','123456','pc_data')
cursor = db.cursor()
#总页数+1
countPage = 14

def get_HTML():
    #首页
    page = 1
    pid = 1
    #每循环一次就可以爬取一个页面数据
    while page<countPage:
        #目标地址
        url="http://www.bjtsb.gov.cn/index.asp?page=" + str(page) + "&KindID=1422&LKindID=0&ClassID=0"
        url1="http://www.bjtsb.gov.cn/"
        response = requests.get(url)
        response.encoding='gbk'
        rtext=response.text
        til = BeautifulSoup(rtext,'html.parser')
        listnum = til.find_all('td',class_='td-dotline')
        #每循环一次可获取一条数据
        for item in range(len(listnum)):
            #获取标题数据
            titles = listnum[item].a
            ti = titles.string.encode('utf-8')
            #获取超连接地址
            aurl = url1 + titles['href']
            sql = "INSERT INTO data (url) VALUE ('" + str(aurl) + "')"
            cursor.execute(sql)
            #print aurl
            promulgator='北京市质量技术监督局'
            sql="UPDATE data SET promulgator =%s WHERE id =%s"
            cursor.execute(sql,(promulgator,pid))
            #获取更新时间
            pubtime = str(listnum[item])[-18:-8]
            sql = "UPDATE data SET pubtime ='"+ pubtime +"' WHERE id ="+str(pid)
            cursor.execute(sql)
            sql = "UPDATE data SET title = %s WHERE id =%s"
            cursor.execute(sql,(ti,pid))
            pid = pid+1
        page=page+1
    db.commit()
    #cursor.close()
    #db.close()
    print pid
get_HTML()

def son_HTML():
    #根据URL爬出子叶面内容
    #数据库中查询所有子页url
    sql = 'SELECT url FROM data'
    cursor.execute(sql)
    urltup = cursor.fetchall()
    #循环每个子页内容
    for num in range(len(urltup)):
        response = requests.get(list(urltup[num])[0])
        response.encoding='gbk'
        rtext=response.text
        sonHt = BeautifulSoup(rtext,'html.parser')
        son_div = sonHt.find('div',class_='font12')
        son_p = son_div.find_all('p')
        # print len(son_p)
        # print son_p.string
        for n in son_p:
            #print n
            son_art = ''
            if n.attrs == {'align':'right'} or n.attrs == {'align':'center'} or n.attrs == {'align':'left'}:
                break
            else:
                son_art = son_art+n.text.encode("utf-8")
                
        sql = "UPDATE data SET article = '"+str(son_art)+"' WHERE id = "+str(num)
        cursor.execute(sql)
        
    db.commit()
    cursor.close()
    db.close()
son_HTML()
    