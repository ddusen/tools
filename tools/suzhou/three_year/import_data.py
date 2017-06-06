# -*- coding: utf-8 -*-
import re
import xlrd
import xlwt
import uuid
from datetime import date, datetime

from openpyxl.reader.excel import load_workbook as lw

from mysql import query, query_one, save

def read_xls(xls_path):
    workbook = xlrd.open_workbook(xls_path)

    # get sheel
    sheet1_name = workbook.sheet_names()[0]

    # accoding to sheel get sheel content
    sheet1 = workbook.sheet_by_index(0)  # sheet index begin 0

    sheetName = sheet1.name  # sheet's name
    rownum = sheet1.nrows  # row number
    colnum = sheet1.ncols  # col number
    colnames = sheet1.row_values(0)

    print 'sheetName = %s , rownum = %s, colnum = %s' % (sheetName, rownum, colnum)

    data_row = []
    for i in xrange(1, rownum):
        data_row.append(sheet1.row_values(i))

    return data_row

def save_product_details(item):
    name = item[5]
    specifications_model = item[7]
    brand = item[8]
    batch_number = item[9]
    grade = u'—'
    is_export_product = 0
    is_quality_product = 1 
    productdetails = query(sql=u'''SELECT id FROM base_productdetails WHERE name=%s''', list1=(name, ))
    if len(productdetails) != 0:
        return productdetails[0].get('id')
    else:
        save(sql=u'''INSERT INTO `base_productdetails`(`name`, `specifications_model`, `brand`, `batch_number`, `grade`,  `is_export_product`, `is_quality_product`)VALUES(%s, %s, %s, %s, %s, %s, %s)''', list1=(name, specifications_model, brand, batch_number, grade, is_export_product, is_quality_product))
        return save_product_details(item) 

def save_sampling(item, guid, check_year):
    check_test_based = u'—'
    check_year = check_year
    check_quarterly = u'—'
    check_type = item[14]
    check_result = item[15]
    check_daterange = check_year
    check_agencies = item[18]
    check_content = u'—'
    check_level = item[19]
    prev_year_sales = u'—'
    failed_item1 = u'—'
    failed_item2 = u'—'
    system_certification = u'—'
    product_certification = u'—'
    safety_certificate = u'—'
    permit_certificate = u'—'
    sampling = query(sql=u'''SELECT id FROM base_sampling WHERE guid=%s''', list1=(guid, ))
    if len(sampling) != 0:
        return sampling[0].get('id')
    else:
        product_details = save_product_details(item)
        save(sql=u'''INSERT INTO `base_sampling`(`guid`, `check_test_based`, `check_year`, `check_quarterly`, `check_type`, `check_result`, `check_daterange`, `check_agencies`, `check_content`, `check_level`, `prev_year_sales`, `failed_item1`, `failed_item2`, `system_certification`, `product_certification`, `safety_certificate`, `permit_certificate`, `product_details_id`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', list1=(guid, check_test_based, check_year, check_quarterly, check_type, check_result, check_daterange, check_agencies, check_content, check_level, prev_year_sales, failed_item1, failed_item2, system_certification, product_certification, safety_certificate, permit_certificate, product_details) )
        return save_sampling(item, guid, check_year)

def query_samplingproduct(name):
    samplingproduct = query(sql=u'''SELECT id FROM base_samplingproduct WHERE name=%s''', list1=(name, ))
    if len(samplingproduct) != 0:
        return samplingproduct[0].get('id')
    else:
        print name
        return 0

def save_enterprise(item):
    organid = uuid.uuid4().hex
    code = uuid.uuid4().hex
    business_license_no = u'—'
    socialcode = u'—'
    name = item[0]
    economic_type = u'—'
    sys_user_id = u'—'
    enterprise_man = u'—'
    sldjlx = u'—'
    zl = u'—'
    principal = u'—'
    dbrzjlx = u'—'
    dbrzjhm = u'—'
    zczj = u'—'
    sshymc = u'—'
    jyfw = u'—'
    fzjgmc = u'—'
    fzrq = u'—'
    hzrq = u'—'
    xxlybm = u'—'
    tgdwqc = u'—'
    address = item[2]
    city = u'苏州市'
    district = item[3]
    post = u'—'
    tel = u'—'
    phone = u'—'
    scale = 0
    is_pass_quality_system = 0
    quality_system_number = u'—'
    no_sampling_records = 1
    three_year_not_sampling = 1
    is_not_license = 1
    is_famous_enterprise = 0
    is_administrative_penalties = 0
    
    enterprise = query(sql=u'''SELECT id FROM base_enterprise WHERE name=%s''', list1=(name, ))
    
    if len(enterprise) != 0:
        return enterprise[0].get('id')
    else:
        save(sql=u'''INSERT INTO `base_enterprise`(`organid`, `code`, `business_license_no`, `socialcode`, `name`, `economic_type`, `sys_user_id`, `enterprise_man`, `sldjlx`, `zl`, `principal`, `dbrzjlx`, `dbrzjhm`, `zczj`, `sshymc`, `jyfw`, `fzjgmc`, `fzrq`, `hzrq`, `xxlybm`, `tgdwqc`, `address`, `city`, `district`, `post`, `tel`, `phone`, `scale`, `is_pass_quality_system`, `quality_system_number`, `no_sampling_records`, `three_year_not_sampling`, `is_not_license`, `is_famous_enterprise`, `is_administrative_penalties`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', list1=(organid, code, business_license_no, socialcode, name, economic_type, sys_user_id, enterprise_man, sldjlx, zl, principal, dbrzjlx, dbrzjhm, zczj, sshymc, jyfw, fzjgmc, fzrq, hzrq, xxlybm, tgdwqc, address, city, district, post, tel, phone, scale, is_pass_quality_system, quality_system_number, no_sampling_records, three_year_not_sampling, is_not_license, is_famous_enterprise, is_administrative_penalties,))
        return save_enterprise(item)

def save_samplingproductenterprise(item, check_year):
    enterprise_id = save_enterprise(item)
    sampling_id = save_sampling(item, str(uuid.uuid4()), check_year)
    sampling_product_id = query_samplingproduct(item[6])

    if not sampling_product_id:
        return 0
    else:
        samplingproductenterprise = query(sql=u'''SELECT id FROM base_samplingproductenterprise WHERE enterprise_id = %s AND sampling_id =%s AND sampling_product_id = %s''', list1=(enterprise_id, sampling_id, sampling_product_id, ))
        if len(samplingproductenterprise) != 0:
            return 0
        else:
            return save(sql=u'''INSERT INTO `base_samplingproductenterprise`(`enterprise_id`, `sampling_id`, `sampling_product_id`) VALUES(%s, %s, %s)''', list1=(enterprise_id, sampling_id, sampling_product_id, ))

def insert_data_2015_country():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2015国抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2015'):
            continue

def insert_data_2015_province():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2015省抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2015'):
            continue

def insert_data_2015_city():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2015市抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2015'):
            continue

def insert_data_2016_country():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2016国抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2016'):
            continue

def insert_data_2016_province():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2016省抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2016'):
            continue

def insert_data_2016_city():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/three_year/2016市抽苏州.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if not save_samplingproductenterprise(item, u'2016'):
            continue


def main():
    insert_data_2015_country()
    insert_data_2015_province()
    insert_data_2015_city()
    insert_data_2016_country()
    insert_data_2016_province()
    insert_data_2016_city()
    
if __name__ == '__main__':
    main()