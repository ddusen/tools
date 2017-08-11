#coding:utf-8
#@author chjsun
#区域 企业 产品
import os
import requests
import jieba
import jieba.posseg as pseg
from bosonnlp import BosonNLP
pointer = 0
tokenLength = 0
tokenNumber = 0
connectionTag = 0

def TokenArray():
    return [
        'A4xzCRD2.4349.eTvL-N6tJl7E',
        '13Sq8yra.4345.0A2LME3k-vlx',
    ]


def getTokenArrayLen():
    return len(TokenArray())


def init():
    global tokenLength, tokenNumber
    tokenLength = getTokenArrayLen()
    tokenNumber = 0


def getToken():
    global pointer
    tokens = TokenArray()
    foot = len(tokens) - 1
    if pointer > foot:
        pointer = 0
    nlp = tokens[pointer]
    pointer += 1
    return nlp


# def jbLocation(results, string):
#     # jieba.enable_parallel(2)
#     seg_list = pseg.cut(string)
#     for word, flag in seg_list:
#         if 'area'==flag:
#             results['location'].append(word.encode("utf-8"))
#         if 'ns'==flag:
#             a = word.encode("utf-8")
#             if a[-3:] in ('国', '省', '市', '县', '城', '区'):
#                 results['location'].append(a)
#     # jieba.enable_parallel()
#     return results


def getConnection():
    global tokenLength, tokenNumber, connectionTag
    count = 0
    token = getToken()
    headers = {'X-Token': token}
    RATE_LIMIT_URL = 'http://api.bosonnlp.com/application/rate_limit_status.json'
    result = requests.get(RATE_LIMIT_URL, headers=headers).json()
    tokenLength = getTokenArrayLen()
    if result['status'] == 200:
        count = result['limits']['ner']['count-limit-remaining']
        if not count:
            if tokenLength > tokenNumber:
                tokenNumber += 1
                return getConnection()
            else:
                init()
                connectionTag = 1
                return None
        return BosonNLP(token)


def getTag(string):
    global connectionTag
    nlp = None
    ners = None
    try:
        init()
        nlp = getConnection()
        ners = nlp.ner(string)[0]
    except Exception, e:
        if connectionTag:
            connectionTag = 0
            return None
        getTag(string)

    if (not nlp) or (not ners):
        return None

    entity = ners.get('entity',[])
    word = ners.get('word',[])

    results = {"org_name": [],
                "company_name": [],
                "product_name": [],
                "location":[],
                "time":[],
                "person_name":[],
                "job_title":[]}

    for ne in entity:
        start = ne[0]
        end = ne[1]
        tag = []
        while end>start:
            tag.append(word[start].encode("utf-8"))
            start+=1
        else:
            results[ne[2]].append("".join(tag))
            tag = []

    # if not results['location']:
    #     results = jbLocation(results, string)
    return results


def test():
    HEADERS = {'X-Token': 'A4xzCRD2.4349.eTvL-N6tJl7E'}
    RATE_LIMIT_URL = 'http://api.bosonnlp.com/application/rate_limit_status.json'
    result = requests.get(RATE_LIMIT_URL, headers=HEADERS).json()


if __name__ == '__main__':
    # getTag("string")
    pass
    # getConnection()
    # for i in xrange(200):
    # string = u"&nbsp; &nbsp; 日前，广东广州检验检疫局驻邮局办事处在对跨境电商备货模式中的安抚奶嘴抽查中发现，一批样品“挡板测试”检测结果不符合GB28482-2012婴幼儿安抚奶嘴安全要求。目前已依法对该批产品作退运处理。<p>&nbsp; &nbsp; “安抚奶嘴”是用来满足儿童非营养性吸吮需要的奶嘴。而“挡板测试”则是衡量婴幼儿安抚奶嘴是否安全的重要检测项目。若该项目测试不合格，则表示安抚奶嘴存在缺陷，有误吸入风险，可能造成婴幼儿窒息。</p><p>&nbsp; &nbsp; 近年来，各国对婴幼儿安抚奶嘴的质量安全问题都比较重视，欧盟委员会非食品快速预警系统曾对多个品牌的安抚奶嘴发出消费警告。质检总局和国家标准化管理委员会曾联合发布了我国首个有关婴幼儿安抚奶嘴的国家强制性标准GB28482-2012《婴幼儿安抚奶嘴安全要求》，对安抚奶嘴的材料结构、机械性能、化学性能及其测试方法等作出了详细规定，也为消费者选择安全优质的安抚奶嘴提供了标准和依据。</p><p>&nbsp; &nbsp; 据介绍，广州局今年对从跨境电商渠道进口的儿童用品进行了专项抽查，其中儿童食品接触产品抽查3批，不合格率为100%。消费者在购买儿童食品接触产品时还须谨慎。</p><p>&nbsp; &nbsp; （王 静 李鹏程）</p><p>&nbsp; &nbsp; 《中国国门时报》<br /></p>"
    # string = u"&nbsp; &nbsp; 日前，广东广州检验检疫局驻邮局办事处在对跨境电商备货模式中的安抚奶嘴抽查中发现，质检总局 一批样品“挡板测试”检测结果不符合GB28482-2012婴幼儿安抚奶嘴安全要求。目前已依法对该批产品作退运处理。<p>&nbsp; &nbsp; “安抚奶嘴”是用来满足儿童非营养性吸吮需要的奶嘴。质检总局 而“挡板测试”则是衡量婴幼儿安抚奶嘴是否安全的重要检测项目。若该项目测试不合格，则表示安抚奶嘴存在缺陷，有误吸入风险，可能造成婴幼儿窒息。</p><p>&nbsp; &nbsp; 近年来，各国对婴幼儿安抚奶嘴的质量安全问题都比较重视，欧盟委员会非食品快速预警系统曾对多个品牌的安抚奶嘴发出消费警告 质检总局。质检总局和国家标准化管理委员会曾联合发布了我国首个有关婴幼儿安抚奶嘴的国家强制性标准GB28482-2012《婴幼儿安抚奶嘴安全要求》，对安抚奶嘴的材料结构、机械性能、化学性能及其测试方法等作出了详细规定，也为消费者选择安全优质的安抚奶嘴提供了标准和依据。</p><p>&nbsp; &nbsp; 据介绍，广州局今年对从跨境电商渠道进口的儿童用品进行了专项抽查，其中儿童食品接触产品抽查3批，不合格率为100%。消费者在购买儿童食品接触产品时还须谨慎。</p><p>&nbsp; &nbsp; （王 静 李鹏程）</p><p>&nbsp; &nbsp; 《中国国门时报》<br /></p>"
    # string = "广东广州检验检疫局驻邮局办事处在对跨境电商备货模式中的安抚奶嘴抽查"
    # for x in getTag(string)['org_name']:
