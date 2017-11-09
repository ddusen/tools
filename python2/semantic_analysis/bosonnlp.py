#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals

import json
import requests

TOKEN = 'kOOze9uF.9476.mEQLFUou6dqs'

#分词
def tag():
	TAG_URL = 'http://api.bosonnlp.com/tag/analysis'
	# 如果某个选项采用默认设置，可以在TAG_URL中省略，完整的TAG_URL如下：
	# 'http://api.bosonnlp.com/tag/analysis?space_mode=0&oov_level=3&t2s=0&special_char_conv=0'
	# 修改space_mode选项为1
	# TAG_URL = \
	#   'http://api.bosonnlp.com/tag/analysis?space_mode=1'
	# 修改oov_level选项为1
	# TAG_URL = \
	#    'http://api.bosonnlp.com/tag/analysis?oov_level=1'
	# 修改t2s选项为1
	# TAG_URL= \
	#     'http://api.bosonnlp.com/tag/analysis?t2s=1'
	# 修改special_char_conv选项为1
	# TAG_URL= \
	# 'http://api.bosonnlp.com/tag/analysis?special_char_conv=1'

	s = ['家具加工、制造、销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）']
	data = json.dumps(s)
	headers = {'X-Token': TOKEN}
	resp = requests.post(TAG_URL, headers=headers, data=data.encode('utf-8'))


	for d in resp.json():
	    print(' '.join(['%s/%s' % it for it in zip(d['word'], d['tag'])]))

#关键词提取
def keywords():
	KEYWORDS_URL = 'http://api.bosonnlp.com/keywords/analysis'

	# text = '机动车综合性能检测（有效期以许可证为准）；机动车尾气检测；机动车安全性能检测。(依法须经批准的项目，经相关部门批准后方可开展经营活动)'
	text = '家具加工、制造、销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）'
	params = {'top_k': 10}
	data = json.dumps(text)
	headers = {'X-Token': TOKEN}
	resp = requests.post(KEYWORDS_URL, headers=headers, params=params, data=data.encode('utf-8'))


	for weight, word in resp.json():
	    print(weight, word)

#命名实体识别
def ner():
	NER_URL = 'http://api.bosonnlp.com/ner/analysis'


	s = ['家具加工、制造、销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）']
	data = json.dumps(s)
	headers = {'X-Token': TOKEN}
	resp = requests.post(NER_URL, headers=headers, data=data.encode('utf-8'))


	for item in resp.json():
	    for entity in item['entity']:
	        print(''.join(item['word'][entity[0]:entity[1]]), entity[2])

if __name__ == '__main__':
	# tag()
	# keywords()
	# ner()