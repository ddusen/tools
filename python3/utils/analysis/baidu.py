'''
    中文语义分析
'''
import json
import requests
import random

from aip import AipNlp


# baidu 中文情感分析
def baidu_emotion(my_str):
    """ 你的 APPID AK SK """
    key1 = {
        'APP_ID': '10801558', 
        'API_KEY': 'FCUZBiFKi4MZO4WnpzU5XeG9', 
        'SECRET_KEY': 't9IVKaYsQzosWwh9EugqBLXmb78P5ei7', 
    }
    key2 = { 
        'APP_ID': '10801769', 
        'API_KEY': 'IsfNeTsr4Y6osB910RmGiKuG', 
        'SECRET_KEY': 'li2NoLMtZi5rUDkrbwGz1z1IR2xhfxyW',
    }
    key3 = {
        'APP_ID': '10862510', 
        'API_KEY': 'QjIRtECSCVrgAGh5AxU63u4Z', 
        'SECRET_KEY': 'iheVvaZqSFSfwtQFkXcQtt0P056RECuU',
    }

    cur_key = random.choice([key1, key2, key3])
    
    client = AipNlp(cur_key['APP_ID'], cur_key['API_KEY'], cur_key['SECRET_KEY'])
    '''
    response result like this:
    {
    "text":"苹果是一家伟大的公司",
    "items":[
        {
            "sentiment":2,    //表示情感极性分类结果
            "confidence":0.40, //表示分类的置信度
            "positive_prob":0.73, //表示属于积极类别的概率
            "negative_prob":0.27  //表示属于消极类别的概率
        }
    ]
    }
    '''

    return client.sentimentClassify(my_str)
