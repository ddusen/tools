'''
    中文语义分析
'''
import json
import requests
import random

from aip import AipNlp


# BosonNLP 中文情感分析
def boson_emotion(my_str):

    SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis?weibo'

    headers = {'X-Token': 'kOOze9uF.9476.mEQLFUou6dqs'}

    data = json.dumps(my_str)
    resp = requests.post(
        SENTIMENT_URL,
        headers=headers,
        data=data.encode('utf-8')
    )

    return resp.json()

