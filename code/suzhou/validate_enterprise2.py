# -*- coding: utf-8 -*-
import sys
import time
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')

from process import (get_response, )


enterprise_name_list = [u'江苏沙钢集团有限公司', 
                        u'江苏永钢集团有限公司', 
                        u'张家港联合铜业有限公司', 
                        u'中粮东海粮油工业（张家港）有限公司', 
                        u'张家港浦项不锈钢有限公司', 
                        u'华芳集团有限公司', 
                        u'张家港协鑫集成科技有限公司', 
                        u'江苏骏马集团有限责任公司', 
                        u'澳洋集团有限公司', 
                        u'江苏华昌（集团）有限公司', 
                        u'攀华集团有限公司', 
                        u'张家港康得新光电材料有限公司', 
                        u'烨辉（中国）科技材料有限公司', 
                        u'波司登股份有限公司', 
                        u'江苏隆力奇集团有限公司', 
                        u'芬欧汇川(中国)有限公司', 
                        u'华普电子（常熟）有限公司', 
                        u'江苏梦兰集团有限公司', 
                        u'夏普办公设备（常熟）有限公司', 
                        u'达富电脑（常熟）有限公司', 
                        u'丰田汽车（常熟）零部件有限公司', 
                        u'江苏常熟发电有限公司', 
                        u'三菱电机汽车部件（中国）有限公司', 
                        u'奇瑞捷豹路虎汽车有限公司', 
                        u'常熟市龙腾特种钢有限公司', 
                        u'江苏理文造纸有限公司', 
                        u'常熟市汽车饰件股份有限公司', 
                        u'达明电子（常熟）有限公司', 
                        u'江苏通润机电集团有限公司', 
                        u'中利科技集团股份有限公司', 
                        u'长春化工（江苏）有限公司', 
                        u'四海电子（昆山）有限公司', 
                        u'仁宝信息技术（昆山）有限公司', 
                        u'圣美精密工业（昆山）有限公司', 
                        u'纬创资通（昆山）有限公司', 
                        u'通力电梯有限公司', 
                        u'乐金电子（昆山）有限公司', 
                        u'利乐包装（昆山）有限公司', 
                        u'昆山丘钛微电子科技有限公司', 
                        u'正新橡胶（中国）有限公司', 
                        u'昆山专用汽车制造厂有限公司', 
                        u'南亚电子材料（昆山）有限公司', 
                        u'牧田（昆山）有限公司', 
                        u'三一重机有限公司', 
                        u'昆山德力铜业有限公司', 
                        u'台光电子材料（昆山）有限公司', 
                        u'昆山龙腾光电有限公司', 
                        u'富士康（昆山）电脑接插件有限公司', 
                        u'淳华科技（昆山）有限公司', 
                        u'好孩子儿童用品有限公司', 
                        u'昆山扬皓光电有限公司', 
                        u'昆山联滔电子有限公司', 
                        u'微盟电子（昆山）有限公司', 
                        u'江苏沙钢集团有限公司', 
                        u'江苏永钢集团有限公司', 
                        u'张家港联合铜业有限公司', 
                        u'中粮东海粮油工业（张家港）有限公司', 
                        u'张家港浦项不锈钢有限公司', 
                        u'华芳集团有限公司', 
                        u'张家港协鑫集成科技有限公司', 
                        u'江苏骏马集团有限责任公司', 
                        u'澳洋集团有限公司', 
                        u'江苏华昌（集团）有限公司', 
                        u'攀华集团有限公司', 
                        u'张家港康得新光电材料有限公司', 
                        u'烨辉（中国）科技材料有限公司', 
                        u'波司登股份有限公司', 
                        u'江苏隆力奇集团有限公司', 
                        u'芬欧汇川(中国)有限公司', 
                        u'华普电子（常熟）有限公司', 
                        u'江苏梦兰集团有限公司', 
                        u'夏普办公设备（常熟）有限公司', 
                        u'达富电脑（常熟）有限公司', 
                        u'丰田汽车（常熟）零部件有限公司', 
                        u'江苏常熟发电有限公司', 
                        u'三菱电机汽车部件（中国）有限公司', 
                        u'奇瑞捷豹路虎汽车有限公司', 
                        u'常熟市龙腾特种钢有限公司', 
                        u'江苏理文造纸有限公司', 
                        u'常熟市汽车饰件股份有限公司', 
                        u'达明电子（常熟）有限公司', 
                        u'江苏通润机电集团有限公司', 
                        u'中利科技集团股份有限公司', 
                        u'长春化工（江苏）有限公司', 
                        u'四海电子（昆山）有限公司', 
                        u'仁宝信息技术（昆山）有限公司', 
                        u'圣美精密工业（昆山）有限公司', 
                        u'纬创资通（昆山）有限公司', 
                        u'通力电梯有限公司', 
                        u'乐金电子（昆山）有限公司', 
                        u'利乐包装（昆山）有限公司', 
                        u'昆山丘钛微电子科技有限公司', 
                        u'正新橡胶（中国）有限公司', 
                        u'昆山专用汽车制造厂有限公司', 
                        u'南亚电子材料（昆山）有限公司', 
                        u'牧田（昆山）有限公司', 
                        u'三一重机有限公司', 
                        u'昆山德力铜业有限公司', 
                        u'台光电子材料（昆山）有限公司', 
                        u'昆山龙腾光电有限公司', 
                        u'富士康（昆山）电脑接插件有限公司', 
                        u'淳华科技（昆山）有限公司', 
                        u'好孩子儿童用品有限公司', 
                        u'昆山扬皓光电有限公司', 
                        u'昆山联滔电子有限公司', 
                        u'微盟电子（昆山）有限公司']

header = {
    'Cookie': 'JSESSIONID=B44F7CAEEBD5A6F29C6DFB666D9E890A',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
url = "http://58.211.125.90:8888/api/%s"

def get_data(request_url):
    result = eval(get_response(request_url, headers=header).text.replace('true', '1').replace('false', '0'))
    if result.get("isSuccess"):
        return result.get("resultData").get("list")
    else:
        return []

def selectJdch(baseEnterpriseName="", baseEnterpriseCode="", baseProductName="", year="", quarter="", checktype="", checkresult="", baseInstitutionName="", checklevel=""):
    request_url = url % "getinspections?baseEnterpriseName=" + baseEnterpriseName + "&baseEnterpriseCode=" + baseEnterpriseCode + "&baseProductName=" + baseProductName + "&year=" + year + "&quarter=" + quarter + "&checktype=" + checktype + "&checkresult=" + checkresult + "&baseInstitutionName=" + baseInstitutionName + "&checklevel=" + checklevel
    return get_data(request_url)
 
def handle_data():
    data = {}
    for enterprise_name in enterprise_name_list:
        year_data_list = []
        for jdch in selectJdch(baseEnterpriseName=enterprise_name):
            year = jdch.get("CHECKYEAR")
            result = "年份: %s, 抽查类型: %s, 产品类别: %s, 产品名称: %s, 抽查结果: %s" % (year, jdch.get("CHECKTYPE"), jdch.get("PRODUCTCATEGORIES"), jdch.get("PRODUCTNAME"), jdch.get("CHECKRESULT"), ) 
            year_data_list.append({
                year: result, 
            })

        data[enterprise_name] = year_data_list

    return data


def main():
    with open("validate_enterprise.txt", "w") as f:
        data = handle_data()
        for k , v in data.items():
            f.write(k.encode('utf-8'))
            f.write("\n")
            if v == []:
                f.write("无该企业抽检记录!")
                f.write("\n")
                f.write("--"*50)
                f.write("\n\n")
                continue
            for item in v:
                for k1, v1 in item.items():
                    f.write(v1)
                    f.write("\n")
            f.write("\n\n")


if __name__ == '__main__':
    main()
