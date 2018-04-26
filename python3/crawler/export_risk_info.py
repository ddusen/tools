import time
import requests

from ciq.utils.crawler import save_export_keywords
from ciq.utils.logger import Logger

'''
scripts/export_risk_info.py -> 出口风险信息 (TBT, SPS, 预警, 召回)

'''

pc_headers = {
    'Cookie': 'sessionid=q953x5ck7rtj4iwi3718c3v1y4ify0ny',
    'Host': 'search.nbciq.gov.cn:808',
    'Referer': 'http://search.nbciq.gov.cn:808/search/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

logger = Logger()

def get_data(url, category):
    params = {
        'turn': '1',
        'categories': '',
        'categoryList': '',
        'timeSpan': '4',
        'departmentType': '{0}_department'.format(category),
        'sortFactor': 'publishDate',
        'keywords': '',
    }

    page = 1
    while page <= 20:
        params['page'] = page

        resp = requests.get(url.format(category), params=params, headers=pc_headers)
        
        try:
            logger.record('Crawler: <scripts/export_risk_info.py> Request <URL: %s>' % (resp.url, ))
            result = resp.json()
        except Exception as e:
            logger.record('export risk info error: %s' % e)
            continue

        lists = result['result']['list']

        if not lists:
            break

        for l in lists:
            save_export_keywords(
                l['entityTags'].split(' '), 
                '{0}...'.format(l['title'][:252]) if len(l['title']) > 250 else l['title'],
                 l['url'],
                 l['publishDate'],
                 l['siteName'],
                 category, 
            )

        time.sleep(1)
        page += 1


def run():
    get_data('http://search.nbciq.gov.cn:808/es/get', 'tbt')
    get_data('http://search.nbciq.gov.cn:808/es/get', 'sps')
    get_data('http://search.nbciq.gov.cn:808/es/get', 'callback')
    get_data('http://search.nbciq.gov.cn:808/es/get', 'warn')
