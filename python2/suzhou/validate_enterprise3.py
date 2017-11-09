# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/sdu/MyProject/tools")

import time

from process import (get_response, )


enterprise_name_list = [u"江苏沙钢集团有限公司", 
                    u"常熟开关制造有限公司", 
                    u"苏州口水娃食品有限公司", 
                    u"江苏亨通光电股份有限公司", 
                    u"科沃斯机器人股份有限公司", 
                    u"苏州东菱振动试验仪器有限公司", 
                    u"苏州工业园区邻里中心发展有限公司", 
                    u"江苏阿仕顿服饰有限公司", 
                    u"苏州金记食品有限公司", 
                    u"江苏正大富通股份有限公司", 
                    u"张家港康得新光电材料有限公司", 
                    u"常熟长城轴承有限公司", 
                    u"苏州佛朗尼齐拉服饰有限公司"]

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
        old_year = ("2003","2004","2005","2006","2007","2008","2009","2010","2012","2013","2014","2015","2016",)
        for y in old_year:
            for jdch in selectJdch(baseEnterpriseName=enterprise_name, year=y):
                if jdch.get("CHECKRESULT") == '不合格':
                    year = jdch.get("CHECKYEAR")
                    result = "年份: %s, 抽查类型: %s, 产品类别: %s, 产品名称: %s, 抽查结果: %s" % (year, jdch.get("CHECKTYPE"), jdch.get("PRODUCTCATEGORIES"), jdch.get("PRODUCTNAME"), jdch.get("CHECKRESULT"), ) 
                    year_data_list.append({
                        year: result, 
                    })
                else:
                    continue

            data[enterprise_name] = year_data_list

    return data


def main():
    with open("validate_enterprise3.txt", "w") as f:
        data = handle_data()
        for k , v in data.items():
            f.write(k.encode('utf-8'))
            f.write("\n")
            if v == []:
                f.write("无该企业不合格抽检记录!")
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
