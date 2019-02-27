# coding: utf-8

from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch([{'host': '106.14.94.38', 'port': 9200}])

    querystring = {
        'sort': 'date',
        'end_date': '2018-12-31',
        'ticket_type': 'order',
        'discount_ids': '4095056320045142017',
        'start_date': '2018-12-01',
        'limit': 1,
        'user': {
            'staff_id': None,
            'name': 'sa',
            'roles': [],
            'is_locked': False,
            'expired': 3599.999997,
            'is_system': True,
            'extends': None,
            'pwd_change_required': False,
            'partner': None,
            'partner_id': 3805520638781685761,
            'id': 3817149127632928799
        },
        'offset': 0,
        'store_ids': '3998950613513248769',
        'order': 'desc',
        '_': '1551174814948'
    }
    start_date = querystring.get('start_date')
    end_date = querystring.get('end_date')
    store_ids = querystring.get('store_ids')  # 门店id
    ticket_type = querystring.get('ticket_type')  # 小票类型
    product_ids = querystring.get('product_id')  # 商品ids
    discount_ids = querystring.get('discount_ids')  # 折扣类型ids
    order_no = querystring.get('order_no')  # 交易编号
    member_no = querystring.get('member_no')  # 会员卡号
    class_name = querystring.get('class_name')  # 交易类型
    payment_ids = querystring.get('payment_ids')  # 支付方式ids
    sort = querystring.get('sort', 'date')  # 排序字段
    order = querystring.get('order', 'desc')  # 排序方式
    offset = querystring.get('offset', '0')  # 页数
    limit = querystring.get('limit', '10')  # 页长

    # format query
    must = []
    if store_ids:
        must.append({
            "bool": {
                "should": {
                    "terms": {
                        "store_id": store_ids.split(',')
                    }
                }
            }
        })
    if product_ids:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body.items",
                  "query":{
                    "bool":{
                      "filter":{
                        "terms":{
                          "payload.body.items.hex_id": product_ids.split(',')
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    if discount_ids:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body.hex_discount_list",
                  "query":{
                    "bool":{
                      "filter":{
                        "terms":{
                          "payload.body.hex_discount_list.id": discount_ids.split(',')
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    if order_no:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body",
                  "query":{
                    "bool":{
                      "filter":{
                        "term":{
                          "payload.body.order_no": order_no
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    if member_no:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body",
                  "query":{
                    "bool":{
                      "should":{
                        "match":{
                          "payload.body.card_no": member_no
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    if class_name:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body",
                  "query":{
                    "bool":{
                      "should":{
                        "match":{
                          "payload.body.dept_class_name": class_name
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    if payment_ids:
        must.append({
            "bool":{
              "filter":{
                "nested":{
                  "path": "payload.body.payments",
                  "query":{
                    "bool":{
                      "filter":{
                        "terms":{
                          "payload.body.payments.hex_id": payment_ids.split(',')
                        }
                      }
                    }
                  }
                }
              }
            }
          })
    sales_date = {}
    if start_date:
        sales_date['gte'] = start_date
    if end_date:
        sales_date['lt'] = end_date
    if sales_date:
        must.append({
          "bool":{
            "filter":{
              "range":{
                "sales_date": sales_date
              }
            }
          }
        })
    body = {
        "query":{
            "bool":{
                "must": must
            }
        },
        "from" : offset,
        "size" : limit,
        "sort": [{"sales_date": order}]
    }  

    result = es.search(index="dq", body=body)

    return result

if __name__ == '__main__':
    main()