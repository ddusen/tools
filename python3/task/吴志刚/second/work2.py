# coding:utf-8
import requests
import bs4
import pymysql

#连接数据库
db = pymysql.connect('192.168.1.131','root','123456','pc_data',use_unicode=True,charset="utf8")
cursor = db.cursor()
#总页数+1
countPage = 14

#获得首页的HTML
def get_HTML():
    #首页
    page = 1
    #数据量,从第一条开始,每循环小循环一次加一条
    pid = 1
    #每循环一次就可以爬取一个页面数据
    while page<countPage:
        #首页目标地址
        url="http://www.bjtsb.gov.cn/index.asp?page=" + str(page) + "&KindID=1422&LKindID=0&ClassID=0"
        #子页请求协议
        url1="http://www.bjtsb.gov.cn/"
        #获取页面HTML
        response = requests.get(url)
        response.encoding='gbk'
        rtext=response.text
        #爬取这个HTML页面,并且用html.parser解析
        til = bs4.BeautifulSoup(rtext,'html.parser')
        #获得本页面所有class=td-dotline 的<td>标签内的文本
        listnum = til.find_all('td',class_='td-dotline')
        #每循环一次可获取一条数据
        for item in range(len(listnum)):
            #获取标题数据
            titles = listnum[item].a
            ti = titles.string.encode('utf-8')
            #获取超连接地址,并存入数据库中
            aurl = url1 + titles['href']
            sql = "INSERT INTO data (id,url) VALUE (%s,%s)"
            cursor.execute(sql,(pid,aurl))
            #发布者都是北京市质量技术监督局,直接在数据库中定义
            promulgator='北京市质量技术监督局'
            sql="UPDATE data SET promulgator =%s WHERE id =%s"
            cursor.execute(sql,(promulgator,pid))
            #获取更新时间,并存入数据库
            pubtime = str(listnum[item])[-17:-5]
            sql = "UPDATE data SET pubtime ='"+ pubtime +"' WHERE id ="+str(pid)
            cursor.execute(sql)
            #将标题存入数据库
            sql = "UPDATE data SET title = %s WHERE id =%s"
            cursor.execute(sql,(ti,pid))
            #循环一次加一,最后是总数据的数目
            pid = pid+1
            #提交
            db.commit()
        #循环一次就爬取了一个页面
        page=page+1
        print ("已经存了%s页" %(page-1))
#获得子页面的HTML
def son_HTML():
    #根据URL爬出子页面内容
    #数据库中查询所有子页url
    sql = 'SELECT url FROM data'
    cursor.execute(sql)
    #将所有uml存在urltup元组里
    urltup = cursor.fetchall()
    #循环每个子页内容
    for num in range(len(urltup)):
        response = requests.get(list(urltup[num])[0])
        response.encoding='gbk'
        rtext=response.text
        sonHt = bs4.BeautifulSoup(rtext,'html.parser')
        #获得本页面所有class=font12 的<div>标签内的文本
        son_div = sonHt.find('div',class_='font12')
        #获取所有在这个<div>里的<p>标签内容
        son_p = son_div.find_all('p')
        #定义一个子页面文章的容器
        son_art = ''
        for n in son_p:
            #过滤掉不属于文章内容的部分
            if n.attrs == {'align':'right'} or n.attrs == {'align':'center'} or n.attrs == {'align':'left'}:
                break
            else:
            #将一个页面属于文章内容合在一起
                son_art = son_art+n.text      
        sql = "UPDATE data SET article = %s WHERE id = %s"
        cursor.execute(sql,(son_art,num+1))
      
        db.commit()
    print ("已经存入%s条数据" %(num+1))
    cursor.close()
    db.close()
get_HTML()
son_HTML()