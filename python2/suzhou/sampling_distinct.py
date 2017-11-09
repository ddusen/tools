# -*- coding: utf-8 -*-
from mysql import query, query_one, save


def handle():
    licenseproductResult = query(sql=u'''SELECT
                                        GROUP_CONCAT(id)
                                        FROM base_sampling GROUP BY 
                                        check_test_based,
                                        check_year,
                                        check_quarterly,
                                        check_type,
                                        check_result,
                                        check_daterange,
                                        check_agencies,
                                        check_content,
                                        check_level,
                                        prev_year_sales,
                                        failed_item1,
                                        failed_item2,
                                        system_certification,
                                        product_certification,
                                        safety_certificate,
                                        permit_certificate,
                                        product_details_id HAVING COUNT(*) > 1''')
    for result in licenseproductResult:
        list1 = result.get("GROUP_CONCAT(id)").split(",")
        listMax = max(list1)
        list1.remove(listMax)
        for li in list1:
            save(
                sql=u'DELETE FROM base_samplingproductenterprise WHERE sampling_id=%s', list1=(li,))
            save(sql=u'DELETE FROM base_sampling WHERE id=%s', list1=(li,))


def main():
    handle()

if __name__ == '__main__':
    main()
