# -*- coding: utf-8 -*-
import sys
sys.path.append("/home/sdu/MyProject/tools")

import time

from process import (get_response, )


enterprise_name_list = [u'江苏新美星包装机械股份有限公司',
            u'江苏海狮机械股份有限公司',
            u'张家港保税区灿勤科技有限公司',
            u'江苏金帆电源科技有限公司',
            u'张家港市国泰华荣化工新材料有限公司',
            u'江苏张家港酿酒有限公司',
            u'江苏金陵体育器材股份有限公司',
            u'张家港中环海陆特锻股份有限公司',
            u'江苏贝尔机械有限公司',
            u'苏州海陆重工股份有限公司',
            u'张家港市新港星科技有限公司',
            u'张家港天达工具有限公司',
            u'江苏爱康实业集团有限公司',
            u'常熟长城轴承有限公司',
            u'苏州通润驱动设备股份有限公司',
            u'常熟通润汽车零部件股份有限公司',
            u'江苏亨通高压海缆有限公司',
            u'江苏格林电器有限公司',
            u'常熟市精工模具制造有限公司',
            u'常熟市天银机电股份有限公司',
            u'英特美光电（苏州）有限公司',
            u'常熟市福莱德连接器科技有限公司',
            u'江苏金龙科技股份有限公司',
            u'常熟市中联光电新材料有限责任公司',
            u'江苏万宝桥梁构件有限公司',
            u'苏州东方模具科技股份有限公司',
            u'苏州维艾普新材料股份有限公司',
            u'苏州新亚科技有限公司',
            u'江苏保捷锻压有限公司',
            u'太仓冠联高分子材料有限公司',
            u'苏州宝骅机械技术有限公司',
            u'太仓海嘉车辆配件有限公司',
            u'太仓荣南密封件科技有限公司',
            u'天顺风能（苏州）股份有限公司',
            u'中广核三角洲（江苏）塑化有限公司',
            u'苏州市富尔达科技股份有限公司',
            u'苏州金辉纤维新材料有限公司',
            u'苏州巨能发电配套设备有限公司',
            u'苏州撼力铜合金材料有限公司',
            u'昆山三景科技股份有限公司',
            u'若宇检具股份有限公司',
            u'昆山佰奥智能装备股份有限公司',
            u'昆山禾信质谱技术有限公司',
            u'苏州领创激光科技有限公司',
            u'昆山开信精工机械股份有限公司',
            u'昆山宝锦激光拼焊有限公司',
            u'江苏中信博新能源科技股份有限公司',
            u'昆山地博光电材料有限公司',
            u'江苏华航威泰机器人科技有限公司',
            u'华天科技（昆山）电子有限公司',
            u'江苏盛纺纳米材料科技股份有限公司',
            u'江苏康沃动力科技股份有限公司',
            u'苏州华源包装股份有限公司',
            u'苏州市佳禾食品工业有限公司',
            u'江苏通鼎宽带有限公司',
            u'吴江变压器有限公司',
            u'苏州捷力新能源材料有限公司',
            u'苏州巨峰电气绝缘系统股份有限公司',
            u'中广核达胜加速器技术有限公司',
            u'通用电梯股份有限公司',
            u'法兰泰克重工股份有限公司',
            u'苏州迈为科技股份有限公司',
            u'江苏凯伦建材股份有限公司',
            u'苏州明志科技有限公司',
            u'苏州绿控传动科技有限公司',
            u'苏州汇川技术有限公司',
            u'苏州斯莱克精密设备股份有限公司',
            u'苏州飞华铝制工业有限公司',
            u'苏州晶瑞化学股份有限公司',
            u'苏州凯尔博精密机械有限公司',
            u'江苏吴中医药集团有限公司',
            u'苏州绿的谐波传动科技有限公司',
            u'苏州环球集团科技股份有限公司',
            u'江苏方邦机械有限公司',
            u'苏州派克顿科技有限公司',
            u'新黎明科技股份有限公司',
            u'艾尔发智能科技股份有限公司',
            u'苏州仕净环保科技股份有限公司',
            u'苏州波发特通讯技术股份有限公司',
            u'苏州市纽克斯照明有限公司',
            u'江苏新安电器有限公司',
            u'苏州六六视觉科技股份有限公司',
            u'莱克电气股份有限公司',
            u'苏州胜利精密制造科技股份有限公司',
            u'苏州华启智能科技有限公司',
            u'苏州路之遥科技股份有限公司',
            u'苏州天孚光通信股份有限公司',
            u'苏州天准科技股份有限公司',
            u'雷允上药业集团有限公司',
            u'苏州恒久光电科技股份有限公司',
            u'苏州兴业材料科技股份有限公司',
            u'苏州艾隆科技股份有限公司',
            u'苏州万龙电气集团股份有限公司',
            u'江苏苏净集团有限公司',
            u'聚灿光电科技股份有限公司',
            u'苏州八方电机科技有限公司',
            u'苏州天华超净科技股份有限公司',
            u'苏州天弘激光股份有限公司',
            u'江南嘉捷电梯股份有限公司',
            u'苏州海格新能源汽车电控系统科技有限公司']

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
