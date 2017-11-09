
# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date, datetime

from openpyxl.reader.excel import load_workbook as lw
from mysql import query, query_one, save


def insert_enterprises():

    workbook = xlrd.open_workbook(r'/home/sdu/MyProject/tools/tools/suzhou/data.xls')

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

    for index, item in enumerate(data_row):
        area = item[1]
        try:
            if save(sql=u"""INSERT INTO `base_area`(`name`) VALUES('%s')""" % (area,)):
                print "INSERT area <%s> SUCCESS!" % (area, )

            area_id = query_one(
                sql=u"""SELECT id FROM `base_area` WHERE `name` = '%s' """ % (area,)).get("id")
        except:
            area_id = query_one(
                sql=u"""SELECT id FROM `base_area` WHERE `name` = '%s' """ %
                (area,)).get("id")

        productcategory = item[13]
        try:
            if save(sql=u"""INSERT INTO `base_productcategory`(`name`) VALUES('%s')""" % (productcategory,)):
                print "INSERT productcategory <%s> SUCCESS!" % (productcategory, )

            product_category_id = query_one(
                sql=u"""SELECT id FROM `base_productcategory` WHERE name = '%s'""" % (productcategory,)).get("id")
        except:
            product_category_id = query_one(sql=u"""SELECT id FROM `base_productcategory`
            WHERE name = '%s'""" % (productcategory,)).get("id")

        try:
            enterprise_name = item[0]
            address = item[2]
            postcode = item[3]
            contact = item[4]
            fixed_telephone = item[5]
            mobile_phone = item[6]
            business_license = item[7]
            organization_code = item[8]
            scale = item[9]
            economy_type = item[10]
            license_authentication = item[11]
            certificate_number = item[12]
            area = area_id

            if save(sql=u"""INSERT INTO `base_enterprise`(`name`,`address`,`postcode`,`contact`,`fixed_telephone`,`mobile_phone`,`business_license`,`organization_code`,`scale`,`economy_type`,`license_authentication`,`certificate_number`,`area_id`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (enterprise_name, address, postcode, contact, fixed_telephone, mobile_phone, business_license, organization_code, scale, economy_type, license_authentication, certificate_number, area,)):
                print "INSERT enterprise <%s> SUCCESS!" % (enterprise_name, )

            enterprise_id = query_one(
                sql=u"""SELECT id FROM  `base_enterprise` WHERE name = '%s' """ % (enterprise_name, )).get("id")
        except:
            enterprise_id = query_one(
                sql=u"""SELECT id FROM  `base_enterprise` WHERE name = '%s' """ % (enterprise_name, )).get("id")

        try:
            product_name = item[14]
            brand = item[15]
            specification = item[16]
            level = item[17]
            manufacture_date = item[18]
            batch_number = item[19]
            sales_volume = item[20]
            productcategory = product_category_id

            if save(sql=u"""INSERT INTO `base_product`(`name`, `brand`, `specification`, `level`, `manufacture_date`,`batch_number`, `sales_volume`, `product_category_id`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (product_name, brand, specification, level, manufacture_date, batch_number, sales_volume, productcategory,)):
                print "INSERT product <%s> SUCCESS!" % (product_name, )

            product_id = query_one(sql=u"""SELECT id FROM `base_product` WHERE name = '%s'""" % (product_name, )).get("id")
        except Exception as e:
            product_id = query_one(sql=u"""SELECT id FROM `base_product` WHERE name = '%s'""" % (product_name, )).get("id")

        if save(sql=u"""INSERT INTO `base_productenterprise`(`enterprise_id`, `product_id`) VALUES(%s, %s)""" % (enterprise_id, product_id, )):
            print "INSERT <%s, %s> SUCCESS!" % (product_name, enterprise_name)


def main():
    # insert_enterprises()
    pass


if __name__ == '__main__':
    main()
