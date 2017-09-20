#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')
from process import get_response


def main():
	header = {
		'Cookie' : 'pgv_pvi=3929355264; RK=gUvmuil6QY; ptui_loginuin=951545814@qq.com; pgv_si=s3783495680; pt2gguin=o0951545814; uin=o0951545814; skey=@Sc03BYfQc; ptisp=ctc; ptcz=5ee2628b16a1d4de5bfc5ba01040878c958d49412edb5d4472031c5557be638d',
		'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	}
	data = {
		'api': 2, 
		'body_data': {"code":2097152,"text":"研发、设计及生产电子专用设备、测试仪器、真空吸尘器及其零配件；销售自产产品并提供相应的技术和检测服务；从事与本企业生产同类产品的商业批发及进出口业务（不涉及国营贸易管理商品，涉及配额、许可证管理商品的，按国家有关规定办理...","type":1}
	}

	r = get_response("http://nlp.qq.com/public/wenzhi/api/common_api1469449716.php", headers=header, data=data)

	print r.text

if __name__ == '__main__':
	main()