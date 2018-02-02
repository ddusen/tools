import time
import random
import requests
import hmac
import hashlib
import base64

from datetime import datetime
from urllib.parse import urlencode, quote_plus
from collections import OrderedDict

config = {
    'SecretId': 'your_secretId',
    'SecretKey': 'your_secretKey',
    'cdbId': 'cdb-ko3zdkzs',
    'Timestamp': int(time.mktime(time.strptime(time.asctime(time.localtime(time.time())), "%a %b %d %H:%M:%S %Y"))),
    'Nonce': random.randint(9999, 100000),
}


def generate_signature():
    payload = {'Action': "DescribeCdbInstances",
               'Nonce': config['Nonce'],
               'Region': "ap-guangzhou",
               'SecretId': config['SecretId'],
               'SignatureMethod': "HmacSHA256",
               'Timestamp': config['Timestamp'],
               'cdbInstanceIds.0': config['cdbId']}

    new_str = 'GETcdb.api.qcloud.com/v2/index.php?{0}'.format(
        urlencode(payload, quote_via=quote_plus))

    hash_sha256 = hmac.new(b'your_secretKey', msg=new_str.encode(
        'utf-8'), digestmod=hashlib.sha256).digest()

    signature = base64.b64encode(hash_sha256).decode()

    return signature


def instances_list():
    req_url = 'https://cdb.api.qcloud.com/v2/index.php'
    params = {
        'Action': 'DescribeCdbInstances',
        'SecretId': config['SecretId'],
        'Region': 'ap-guangzhou',
        'Timestamp': config['Timestamp'],
        'Nonce': config['Nonce'],
        'Signature': generate_signature(),
        'SignatureMethod': 'HmacSHA256',
        'cdbInstanceIds.0': config['cdbId'],
    }
    print(params)
    r = requests.get(req_url, params=params)
    print(r.url)
    return r.json()


def backup_list():
    req_url = 'https://cdb.api.qcloud.com/v2/index.php'
    params = {
        'Action': 'GetCdbExportLogUrl',
        'SecretId': config['SecretId'],
        'Region': 'ap-guangzhou',
        'Timestamp': config['Timestamp'],
        'Nonce': config['Nonce'],
        'Signature': generate_signature(),
        'SignatureMethod': 'HmacSHA256',
        'cdbInstanceIds.0': config['cdbId'],
        'type': 'coldbackup',
    }
    print(params)
    r = requests.get(req_url, params=params)
    print(r.url)

    print(r.json())


def job_list():
    req_url = 'https://cdb.api.qcloud.com/v2/index.php'
    params = {
        'Action': 'GetCdbJobList',
        'SecretId': config['SecretId'],
        'Region': 'ap-guangzhou',
        'Timestamp': config['Timestamp'],
        'Nonce': config['Nonce'],
        'Signature': generate_signature(),
    }
    print(params)
    r = requests.get(req_url, params=params)
    print(r.url)

    print(r.json())


def main():
    print(instances_list())


if __name__ == '__main__':
    main()
