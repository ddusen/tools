import time
import random
import requests
import hmac
import hashlib
import base64

from datetime import datetime
from urllib.parse import quote_plus
from collections import OrderedDict

config = {
    'SecretId': 'your_secretId',
    'SecretKey': 'your_secretKey',
    'cdbId': 'cdb-ko3zdkzs',
    'Timestamp': int(time.mktime(time.strptime(time.asctime(time.localtime(time.time())), "%a %b %d %H:%M:%S %Y"))),
    'Nonce': random.randint(9999, 100000),
}


def split_joint(my_dict):
    str1 = '&'
    str2 = '='
    str3 = '?'

    temp_list = []
    for k, v in my_dict.items():
        temp_list.append(str2.join((k, v,)))

    return str3.join(['GETcdb.api.qcloud.com/v2/index.php', str1.join(temp_list)])


def generate_signature():
    origin_params = OrderedDict()

    origin_params["Action"] = "DescribeCdbInstances"
    origin_params["Nonce"] = config['Nonce']
    origin_params["Region"] = "ap-guangzhou"
    origin_params["SecretId"] = config['SecretId']
    origin_params["SignatureMethod"] = "HmacSHA256"
    origin_params["Timestamp"] = config['Timestamp']
    origin_params["cdbInstanceIds.0"] = config['cdbId']

    new_str = split_joint(origin_params)

    hash_sha256 = hmac.new(config['SecretKey'].encode('utf-8'), msg=new_str.encode('utf-8'), digestmod=hashlib.sha256).digest()

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
    r = requests.get(req_url, params=params)

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
        'cdbInstanceId': config['cdbId'],
        'type': 'coldbackup',
    }
    r = requests.get(req_url, params=params)

    return r.json()


def job_list():
    req_url = 'https://cdb.api.qcloud.com/v2/index.php'
    params = {
        'Action': 'GetCdbExportLogUrl',
        'SecretId': config['SecretId'],
        'Region': 'ap-guangzhou',
        'Timestamp': config['Timestamp'],
        'Nonce': config['Nonce'],
        'Signature': generate_signature(),
        'cdbInstanceId': config['cdbId'],
        'type': 'coldbackup',
    }
    r = requests.get(req_url, params=params)

    return r.json()


def main():
    print(instances_list())


if __name__ == '__main__':
    main()