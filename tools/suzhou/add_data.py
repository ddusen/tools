# -*- coding: utf-8 -*-
from mysql import query, query_one, save

institution_name_list = [u'江苏省质量技术监督珠宝首饰产品质量检验站',
                         u'镇江市产品质量监督检验中心',
                         u'国家纺织产品质量监督检验中心（江阴）',
                         u'泰州市产品质量监督检验所',
                         u'江苏省质量技术监督通信产品质量检验站',
                         u'江苏省玻璃制品质量监督检验中心（宿迁）',
                         u'常州市纤维检验所',
                         u'徐州市产品质量监督检验中心',
                         u'盐城市计量测试所',
                         u'盐城市产品质量监督检验所',
                         u'盐城市纤维检验所',
                         u'国家洗漱用品质量监督检验中心',
                         u'江苏省质量技术监督纸张印刷产品质量检验站',
                         u'国家工程复合材料产品质量监督检验中心',
                         u'连云港市产品质量监督检验中心',
                         u'江苏省纺织产品质量监督检验研究院',
                         u'南通市产品质量监督检验所',
                         u'苏州市产品质量监督检验所',
                         u'国家电线电缆产品质量监督检验中心',
                         u'南京市产品质量监督检验院',
                         u'江苏省特种安全防护产品质量监督检验中心',
                         u'宿迁市产品质量监督检验所',
                         u'江苏省泵阀产品质量监督检验中心',
                         u'江苏省特种设备安全监督检验研究院',
                         u'扬州市产品质量监督检验所',
                         u'江苏省产品质量监督检验研究院',
                         u'南通市纤维检验所',
                         u'苏州市纤维检验所',
                         u'国家轻型电动车及电池产品质量监督检验中心',
                         u'江苏省磨料磨具产品质量监督检验中心',
                         u'苏州市质量技术监督综合检验检测中心']


def insert_status():
    data = [u'待确认', u'待抽样', u'待检测', u'待上报', u'已确认', u'已抽样', u'已检测', u'已上报']

    insert_sql = u"""INSERT INTO `postprocess_status`(`id`, `name`) VALUES(%s, %s)"""

    for index, item in enumerate(data):
        if save(sql=insert_sql, list1=(index + 1, item)):
            print "insert status <%s , %s> successful !" % (index + 1, item)


def insert_risk_status():
    data = [u'待确认', u'待抽样', u'待检测', u'待上报', u'已确认', u'已抽样', u'已检测', u'已上报']
    # data = [u'待分配', u'待确认', u'已确认',
    #         u'待抽样', u'已抽到样', u'未抽到样',
    #         u'正在检测', u'完成检测', u'已通知企业',
    #         u'待审核', u'已审核', u'整改审核',
    #         u'完成整改', u'逾期整改', u'正在整改',
    #         u'正在查处', u'完成查处']

    insert_sql = u"""INSERT INTO `risk_status`(`id`, `name`) VALUES(%s, %s)"""

    for index, item in enumerate(data):
        if save(sql=insert_sql, list1=(index + 1, item)):
            print "insert risk_status <%s , %s> successful !" % (index + 1, item)


def insert_group():
    if save(sql=u"INSERT INTO `base_group`(`name`, `level`, `parent_id`) VALUES ('质监局',1,NULL)"):
        print "insert group <质监局> successful!"

    parent_id = query_one(
        sql=u"""SELECT id FROM `base_group` WHERE name = '质监局' """).get('id')
    if save(sql=u"INSERT INTO `base_group`(`name`, `level`, `parent_id`)  VALUES ('苏州质量技术监督局', 2, %s)" % parent_id):
        print "insert group <苏州质量技术监督局> successful!"

    if save(sql=u"INSERT INTO `base_group`(`name`, `level`, `parent_id`)  VALUES ('检测机构',1,NULL)"):
        print "insert group <检测机构> successful!"

    for index, item in enumerate(institution_name_list):
        parent_id = query_one(
            sql=u"""SELECT id FROM `base_group` WHERE name = '检测机构' """).get('id')
        if save(sql=u"INSERT INTO `base_group`(`name`, `level`, `parent_id`)  VALUES('%s', 2, %s)" % (item, parent_id)):
            print "insert group <%s> successful!" % item

    parent_id = query_one(
        sql=u"""SELECT id FROM `base_group` WHERE name = '苏州质量技术监督局' """).get('id')
    if save(sql=u"INSERT INTO `base_group`(`name`, `level`, `parent_id`)  VALUES ('吴江质监',3, %s)" % parent_id):
        print "insert group <吴江质监> successful!"


def insert_user():
    group_id = query_one(
        sql=u"""SELECT id FROM base_group WHERE name = '苏州质量技术监督局'""").get('id')
    if save(sql=u"INSERT INTO `base_user`(`username`, `password`, `last_login`, `is_superuser`, `is_active`, `date_joined`, `group_id`) VALUES ('szzj_1','szzj_1',now(),1,1,now(),%s)" % group_id):
        print "insert user <szzj_1> successful!"

    group_id = query_one(
        sql=u"""SELECT id FROM base_group WHERE name = '苏州质量技术监督局'""").get('id')
    if save(sql=u"INSERT INTO `base_user`(`username`, `password`, `last_login`, `is_superuser`, `is_active`, `date_joined`, `group_id`) VALUES ('szzj_news','szzj_news',now(),1,1,now(),%s)" % group_id):
        print "insert user <szzj_news> successful!"

    group_id = query_one(
        sql=u"""SELECT id FROM base_group WHERE name = '苏州市质量技术监督综合检验检测中心'""").get('id')
    if save(sql=u"INSERT INTO `base_user`(`username`, `password`, `last_login`, `is_superuser`, `is_active`, `date_joined`, `group_id`) VALUES ('institution','institution',now(),1,1,now(),%s)" % group_id):
        print "insert user <institution> successful!"

    group_id = query_one(
        sql=u"""SELECT id FROM base_group WHERE name = '吴江质监'""").get('id')
    if save(sql=u"INSERT INTO `base_user`(`username`, `password`, `last_login`, `is_superuser`, `is_active`, `date_joined`, `group_id`) VALUES ('sz_wjzj_1','sz_wjzj_1',now(),1,1,now(),%s)" % group_id):
        print "insert user <sz_wjzj_1> successful!"


def insert_institution_user():
    for index, item in enumerate(institution_name_list):
        group_id = query_one(
            sql=u"""SELECT id FROM `base_group` WHERE name = '%s' """ % item).get('id')
        if save(sql=u"INSERT INTO `base_institution`(`name`, `code`, `contact`, `address`, `post`, `phone`, `fax`,`group_id`) VALUES ('%s','—','—','—','—','—','—',%s)" % (item, group_id)):
            print "insert institution < %s > successful !" % item
 
def insert_inspection_type():
    data = {
        1: u"市级专项监督抽查",
        2: u"市级定期监督检验",
        3: u"市级市场监督抽查",
        4: u"市级监督抽查",
        5: u"市级风险监测",
    }

    insert_sql = u"""INSERT INTO `postprocess_inspectiontype`(`id`, `name`) VALUES(%s, %s)"""

    for k, v in data.items():
        result = save(sql=insert_sql, list1=(k, v))
        print "insert inspection_type <%s , %s> successful !" % (k, v)


def main():
    insert_status()
    insert_risk_status()
    insert_group()
    insert_user()
    insert_institution_user()
    insert_inspection_type()


if __name__ == '__main__':
    main()
