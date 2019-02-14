import os
import sys
import requests
sys.path.append(os.getcwd())

from utils.office.excel import write_xlsx


def req(url, params={}):
    headers = {
        'authorization': 'Bearer wg-hzlo5MYSOTpVLvFQfgg',
        'Cookie': 'hex_server_session=5ccac48f-b316-4741-932f-767bdba4aebf',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    r = requests.get(url,
                     headers=headers,
                     params=params
                     )

    return r.json()


def process():
    index = 0
    data = [(
        'SPU ID',
        'SPU名称',
        'SKU ID',
        'SKU编号',
        'SKU名称',
        'SPU编号',
        'SKU别名',
        )]
    spu_offset = 0
    spu_url = 'http://dq.hexcloud.cn/api/v1/product'
    spu_params = {
        'code': 'all',
        'filters': '{"sale_type":"SPU"}',
        'include_state': 'true',
        'include_total': 'true',
        'is_task': 'true',
        'relation': 'all',
        'search_fields': 'name,code,relation.product_category.name',
        'stringified': 'true',
        'order': 'asc',
        'limit': '10',
        'state': 'draft,enabled',
        'status': '',
        'include_request': 'true',
        'is_new': 'true',
        'include_state': 'true',
        '_': '1550105760597',
    }
    spu_data_total = req(spu_url, spu_params)['payload']['total']
    while spu_offset <= spu_data_total:
        spu_params['offset'] = spu_offset
        for spu in req(spu_url, spu_params)['payload']['rows']:
            spu_id = spu['id']
            spu_name = spu['name']
            spu_code = spu['code']

            sku_list_url = 'http://dq.hexcloud.cn/api/v1/product/sku?product_id={0}&stringified=true'.format(spu_id)
            sku_list_data = req(sku_list_url)['payload']

            if not sku_list_data:
                data.append((
                    spu_id,
                    spu_name,
                    '',
                    '',
                    '',
                    spu_code,
                    '',
                    ))

            for sku in sku_list_data:
                sku_id = sku['link_product_id']
                if not sku_id:
                    continue

                sku_nickname = sku['name']
                sku_url = 'http://dq.hexcloud.cn/api/v1/product/{0}'.format(sku_id)
                sku_params = {
                    'relation': 'all',
                    'code': 'all',
                    'is_new': 'true',
                    'include_state': 'true',
                    'stringified': 'true',
                }
                sku_data = req(sku_url, sku_params)['payload']

                sku_code = sku_data['code']
                sku_name = sku_data['name']

                data.append((
                    spu_id,
                    spu_name,
                    sku_id,
                    sku_code,
                    sku_name,
                    spu_code,
                    sku_nickname,
                ))
                index += 1
                print(index, '  ', spu_name, sku_name)

        spu_offset += 10

    file = '/mnt/f/SPU商品明细.xlsx'
    write_xlsx(file, data)


def main():
    process()
    

if __name__ == '__main__':
    main()
