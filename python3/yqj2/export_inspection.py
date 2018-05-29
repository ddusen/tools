#!/usr/bin/python3

import os, sys
import openpyxl
from io import BytesIO
sys.path.append(os.getcwd())

from utils.db.mysql import query, query_one, save

def db_config():
    return {
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'passwd':'123456',
        'db':'yqj2'
    }


def main():
    query(sql='')

if __name__ == '__main__':
    print(main())
