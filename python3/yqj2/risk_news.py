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
    #Model weight
    model = {'GUID': 0, '标题': 0, 'URL': 0, '发布时间': 0, '来源': 0, '发布者': 0, '风险程度': 0, '地域': 0, '类别': 0, '行业编号': 0, }
    #sheet value
    sv = lambda x, y, z : z.cell(row=x, column=y).value
    #date format
    def date_format(df):
        try:
            return openpyxl.utils.datetime.from_excel(df)
        except Exception:
            try:
                return str_to_date(df)
            except Exception:
                return df
    try:
        xlsx_book = openpyxl.load_workbook('/mnt/f/work/risk_news.xlsx', read_only=True)
        sheet = xlsx_book.active
        rows = sheet.rows
    except Exception as e:
        return {
                'status': 0, 
                'message': '操作失败！请检查文件是否有误。详细错误信息：%s！' % e
            }
    
    total = 0
    dupli = 0

    for i, row in enumerate(rows):
        i += 1
        if i == 1:
            line = [cell.value for cell in row]
            for k in model.keys():
                model[k] = line.index(k) + 1
        else:
            try:
                title = sv(i, model['标题'], sheet)
                url = sv(i, model['URL'], sheet)
                if not url:
                    continue

                pubtime = date_format(sv(i, model['发布时间'], sheet))
                if not pubtime:
                    return {
                        'status': 0, 
                        'message': '操作失败！Excel %s 行时间格式有误！' % (i + 1, )
                    }
                
                source = sv(i, model['来源'], sheet)
                publisher = sv(i, model['发布者'], sheet)
                score = sv(i, model['风险程度'], sheet)
                area = sv(i, model['地域'], sheet)
                category = sv(i, model['类别'], sheet)
                industry_number = sv(i, model['行业编号'], sheet)

                total += 1
                if query_one(sql='SELECT COUNT(*) FROM `risk_news` WHERE `url` = %s', db_config=db_config(), list1=(url, ))[0]:
                    dupli += 1
                    continue

                if not query_one(sql='SELECT COUNT(*) FROM `risk_news_publisher` WHERE `name` = %s', db_config=db_config(), list1=(source, ))[0]:
                    save(sql='INSERT INTO `risk_news_publisher`(`name`) VALUES(%s, )', db_config=db_config(), list1=(source, ))

                publisher_id = query(sql='SELECT `id` FROM `risk_news_publisher` WHERE `name` = %s', db_config=db_config(), list1=(source, ))[0][0]
                save(sql='INSERT INTO `risk_news`(`title`, `url`, `content`, `pubtime`, `reprinted`, `publisher_id`, `id_delete`, `risk_keyword`, `invalid_keyword`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    db_config=db_config(),
                    list1=(title, url, '', pubtime, 0, publisher_id, 2, '', '', ))

                risk_news_id = query(sql='SELECT `id` FROM `risk_news` WHERE `url`= %s', db_config=db_config(), list1=(url, ))[0][0]
                print(risk_news_id)
                i = 10 / 0 

                areas = area.split(',')
                for a_name in areas:
                    a_queryset = query_one(sql='SELECT COUNT(*) FROM `area` WHERE `name`=%s', db_config=db_config(), list1=(a_name, ))[0]
                    if not a_queryset:
                        return {
                            'status': 0, 
                            'message': '操作失败！Excel %s 行，地域 %s 不存在！' % (i + 1, a_name, )
                        }

                    area_ids = query(sql='SELECT `id` FROM `area` WHERE `name`=%s', db_config=db_config(), list1=(a_name, ))[0]
                    if not query_one(sql='SELECT COUNT(*) FROM `risk_news_area` WHERE `risknews_id` = %s AND `area_id` = %s', db_config=db_config(), list1=(risk_news_id, area_id, )):
                        save(sql='INSERT INTO `risk_news_area`(`risknews_id`, `area_id`) VALUES(%s, %s)', db_config=db_config(), list1=(risknews_id, area_id, ))                       


            except Exception as e:
                return {
                    'status': 0, 
                    'message': '操作失败！Excel %s 行存在问题。详细错误信息：%s！' % (i + 1, e)
                }

    return {
                'status': 1, 
                'message': '操作成功！共处理%s条数据，成功导入%s条数据，重复数据%s条！' % (total, total - dupli, dupli, )
            }

if __name__ == '__main__':
    print(main())
