# -*- coding: utf-8 -*-
from mysql import query, query_one, save


def insert_status():
    data = [u'待分配', u'待确认', u'已确认',
            u'待抽样', u'已抽到样', u'未抽到样',
            u'正在检测', u'完成检测', u'已通知企业',
            u'待审核', u'已审核', u'整改审核',
            u'完成整改', u'逾期整改', u'正在整改',
            u'正在查处', u'完成查处']

    insert_sql = u"""INSERT INTO `postprocess_status`(`id`, `name`) VALUES(%s, %s)"""

    for index, item in enumerate(data):
        if save(sql=insert_sql, list1=(index + 1, item)):
            print "insert status <%s , %s> successful !" % (index + 1, item)


def insert_risk_status():
    data = [u'待分配', u'待确认', u'已确认',
            u'待抽样', u'已抽到样', u'未抽到样',
            u'正在检测', u'完成检测', u'已通知企业',
            u'待审核', u'已审核', u'整改审核',
            u'完成整改', u'逾期整改', u'正在整改',
            u'正在查处', u'完成查处']

    insert_sql = u"""INSERT INTO `risk_status`(`id`, `name`) VALUES(%s, %s)"""

    for index, item in enumerate(data):
        if save(sql=insert_sql, list1=(index + 1, item)):
            print "insert risk_status <%s , %s> successful !" % (index + 1, item)


def insert_group():
    if save(sql=u"INSERT INTO `base_group` VALUES (15,'质监局',1,NULL)"):
        print "insert group <质监局> successful!"

    if save(sql=u"INSERT INTO `base_group` VALUES (16,'苏州质量技术监督局',2,15)"):
        print "insert group <苏州质量技术监督局> successful!"

    if save(sql=u"INSERT INTO `base_group` VALUES (17,'检测机构',1,NULL)"):
        print "insert group <检测机构> successful!"

    if save(sql=u"INSERT INTO `base_group` VALUES (18,'检测机构A',2,17)"):
        print "insert group <检测机构> successful!"

    if save(sql=u"INSERT INTO `base_group` VALUES (19,'吴江质监',3,16)"):
        print "insert group <吴江质监> successful!"


def insert_user():
    if save(sql=u"INSERT INTO `base_user` VALUES (5,'szzj_1','szzj_1',NULL,1,1,'2016-12-13 12:02:46',16)"):
        print "insert user <szzj_1> successful!"

    if save(sql=u"INSERT INTO `base_user` VALUES (6,'institution','institution','2016-12-13 12:20:38',1,1,'2016-12-13 12:20:40',18)"):
        print "insert user <institution> successful!"

    if save(sql=u"INSERT INTO `base_user` VALUES (7,'sz_wjzj_1','sz_wjzj_1','2016-12-13 12:21:34',1,1,'2016-12-13 12:21:35',19)"):
        print "insert user <sz_wjzj_1> successful!"


def insert_bureau_user():
    pass


def insert_institution_user():
    if save(sql=u"INSERT INTO `base_institution` VALUES (1,'检测机构A','address',46566,'ini','1806279',18)"):
        print "insert institution < 检测机构A > successful !"


def insert_inspection_category():
    data = {
        1: u"抽查大类A",
        2: u"抽查大类B",
    }

    insert_sql = u"""INSERT INTO `postprocess_inspectioncategory`(`id`, `name`) VALUES(%s, %s)"""

    for k, v in data.items():
        result = save(sql=insert_sql, list1=(k, v))
        print "insert inspection_category <%s , %s> successful !" % (k, v)


def insert_inspection_type():
    data = {
        1: u"市级监督抽查",
        2: u"市级专项监督抽查",
        3: u"市级风险监测",
    }

    insert_sql = u"""INSERT INTO `postprocess_inspectiontype`(`id`, `name`) VALUES(%s, %s)"""

    for k, v in data.items():
        result = save(sql=insert_sql, list1=(k, v))
        print "insert inspection_type <%s , %s> successful !" % (k, v)


def insert_category():
    if save(sql=u"INSERT INTO `base_category`(`id`, `name`) VALUES(1, '产品类别')") == 1:
        print "insert category < %s > successful !" % '产品类别'

    if save(sql=u"INSERT INTO `base_category`(`id`, `name`) VALUES(2, '产品类别A')") == 1:
        print "insert category < %s > successful !" % '产品类别A'


def insert_area():
    if save(sql=u"INSERT INTO `base_area`(`id`, `name`, `level`) VALUES(1, '中国', 1)") == 1:
        print "insert area < %s > successful !" % '中国'

    if save(sql=u"INSERT INTO `base_area`(`id`, `name`, `level`, `parent_id`) VALUES(2, '河南', 2, 1)") == 1:
        print "insert area < %s > successful !" % '河南'


def insert_product():
    if save(sql=u"INSERT INTO `base_product`(`id`, `name`, `specifications`, `date`, `category_id`, `origin_id`) VALUES(1, '汉堡王', '超大', now(),  2, 2)") == 1:
        print "insert product < %s > successful !" % '汉堡王'


def insert_product_grade():
    if save(sql=u"""INSERT INTO `postprocess_productgrade`(`id`, `name`, `level`) VALUES(1, '残次品', 1)""") == 1:
        print "insert economy < %s > successful !" % '残次品'

    if save(sql=u"""INSERT INTO `postprocess_productgrade`(`id`, `name`, `level`) VALUES(2, '有毒', 1)""") == 1:
        print "insert economy < %s > successful !" % '有毒'


def insert_enterprise():
    if save(sql=u"INSERT INTO `base_enterprise`(`id`, `name`, `address`, `representative`, `postcode`, `contact`, `telephone`, `industry`) VALUES(1, '憨憨包', '汉堡', 1111, 1001, 'admin', 10011, '食品')") == 1:
        print "insert enterprise < %s > successful !" % '河南'

    if save(sql=u"INSERT INTO `base_enterprise`(`id`, `name`, `address`, `representative`, `postcode`, `contact`, `telephone`, `industry`) VALUES(2, '周黑鸭', '黑鸭', 1111, 1001, 'admin', 10011, '食品')") == 1:
        print "insert enterprise < %s > successful !" % '武汉'

    if save(sql=u"INSERT INTO `base_enterprise`(`id`, `name`, `address`, `representative`, `postcode`, `contact`, `telephone`, `industry`) VALUES(3, '白斩鸡', '肉', 1111, 1001, 'admin', 10011, '食品')") == 1:
        print "insert enterprise < %s > successful !" % '北京'


def insert_economy():
    if save(sql=u"INSERT INTO `base_economy`(`id`, `name`) VALUES(1, '餐饮')") == 1:
        print "insert economy < %s > successful !" % '餐饮'


def main():
    insert_status()
    insert_risk_status()
    insert_group()
    insert_user()
    insert_bureau_user()
    insert_institution_user()
    insert_inspection_category()
    insert_inspection_type()
    # insert_category()
    # insert_area()
    # insert_product()
    # insert_product_grade()
    # insert_enterprise()


if __name__ == '__main__':
    main()
