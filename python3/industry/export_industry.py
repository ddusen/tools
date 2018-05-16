import os, sys
sys.path.append(os.getcwd())

from utils.office.excel import write_xlsx
from utils.db.mysql import query, query_one, save


def db_config():
    return {
        'host':'127.0.0.1',
        'port':3306,
        'user':'sud',
        'passwd':'123456',
        'db':'observer',
    }

def process():
    filepath = '/mnt/f/industries.xlsx'
    queryset = query(sql='SELECT CONVERT(`id`, char), `name`, `level`, `desc`, CONVERT(`parent_id`, char) FROM `base_industry`', db_config=db_config())
    write_xlsx(filepath, queryset)

if __name__ == '__main__':
    process()
