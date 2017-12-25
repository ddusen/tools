#coding:utf-8

import requests
from bs4 import Beautifulsoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url='http://www.gsxt.gov.cn/index.html'

header={
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_url():
    page=requests.get(url=url,headers=header)
    page.encoding='gbk'
    text=page.text
    soup=Beautifulsoup(text,'html.parser')
    print (soup)
get_url()


def main():
    driver=webdriver.Chrome(exexutable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome driver.exe")
    driver.get("http://www.gsxt.gov.cn/index.html/")

    WebDriverWait(driver,30).until(lambda the_driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']").is_diaplayed())
    WebDriverWait(driver,30).until(lambda the_driver.find_element_by_xpath("//div[@class='gt_cut_bg gt_show']").is_diaplayed())
    WebDriverWait(driver,30).until(lambda the_driver.find_element_by_xpath("//div[@class='gt_cut_fullbg gt_show']").is_diaplayed()) 

    #找到滑动的圆球
    element=driver.find_element_by_xpath("//div[class='gt_slider_knob gt_show']")
    
    print ("第一步,贴着元素 ")
    Actionchains(driver).click_and_hold(on_element=element).perform()
    time.sleep(1)

    print ("第二步,拖动元素 ")
    Actionchains(driver).move_to_element_with_offset(to_element=element,xoffset=200,yoffset=50).perform()
    time.sleep(2)

    print ("第三步,释放鼠标 ")
    Actionchains(driver).release(on_element=element).perform()
    time.sleep(3)
if __name__=='__main__':
    pass
    main()



raw_input=input("请输入企业名称:")
playword={'wd':'raw_input','ie':'utf-8'}

r=requests.post(url,params=playword)

print(r)
