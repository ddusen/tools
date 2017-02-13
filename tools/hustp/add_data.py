# -*- coding: utf-8 -*-
import random

from mysql import query, query_one, save


def get_last_id():
    return query_one(sql=u"""SELECT `id` FROM `category` ORDER BY `id` DESC LIMIT 0,1 """).get('id')


def print_log(item):
    print "INSERT < %s > SUCCESS!" % item


def import_category():
    level_one_list = [u'本科', u'高职', u'研究生', u'中职']

    level_two_one_list = [u'机械',
                          u'电子电气',
                          u'建筑',
                          u'医学',
                          u'艺术/设计',
                          u'外语/计算机',
                          u'管理学',
                          u'法律/经济/社会/政治',
                          u'文学/哲学/历史/教育',
                          u'工学',
                          u'理学',
                          u'农学',
                          u'公共课']

    level_two_two_list = [u'机械',
                          u'电子电气',
                          u'建筑',
                          u'医学',
                          u'艺术/设计',
                          u'外语/计算机',
                          u'管理学',
                          u'法律/经济',
                          u'文学/教育',
                          u'工学',
                          u'理学',
                          u'农学',
                          u'公共课']
    level_two_three_list = [u'机械', u'电工电子', u'外语', u'人文社科', u'其它']

    level_two_four_list = [u'旅游',
                           u'汽车',
                           u'计算机',
                           u'机电',
                           u'模具',
                           u'数控',
                           u'医学/化学',
                           u'其他']

    level_three_dict_one = {u'机械': [u'材料及工程',
                                    u'机械设计制造及其自动化',
                                    u'机械工程及自动化',
                                    u'测控技术与仪器',
                                    u'能源动力',
                                    u'工程力学',
                                    u'学科基础课'],
                            u'电子电气': [u'通信工程',
                                      u'电子信息工程',
                                      u'微电子科学与工程',
                                      u'光电信息科学与工程',
                                      u'电气工程及其自动化',
                                      u'电子科学与技术',
                                      u'自动化'],
                            u'建筑': [u'土木专业',
                                    u'建筑学',
                                    u'风景园林',
                                    u'城市规划',
                                    u'建筑环境与设备工程',
                                    u'环境设计',
                                    u'环境科学与工程'],
                            u'医学': [u'基础医学',
                                    u'临床医学与医学技术',
                                    u'医学检验',
                                    u'中医学',
                                    u'护理学',
                                    u'药学',
                                    u'医学人文'],
                            u'艺术/设计': [u'基础课与艺术设计理论',
                                       u'动漫设计',
                                       u'音乐',
                                       u'产品设计',
                                       u'环境艺术设计',
                                       u'视觉传达设计'],
                            u'外语/计算机': [u'大学英语',
                                        u'专业英语',
                                        u'英语考试',
                                        u'日语/法语/俄语',
                                        u'计算机基础',
                                        u'计算机科学与技术',
                                        u'软件工程/软件技术',
                                        u'网络安全'],
                            u'管理学': [u'工商管理',
                                     u'市场营销',
                                     u'会计学',
                                     u'电子商务',
                                     u'财务管理',
                                     u'人力资源管理',
                                     u'旅游管理',
                                     u'物流管理',
                                     u'房地产经营管理',
                                     u'公共管理',
                                     u'行政管理',
                                     u'信息管理与信息系统'],
                            u'法律/经济/社会/政治': [u'法学',
                                             u'社会学',
                                             u'政治学',
                                             u'经济学',
                                             u'国际经贸',
                                             u'财政学',
                                             u'金融学',
                                             u'监狱培训'],
                            u'文学/哲学/历史/教育': [u'哲学',
                                             u'历史学',
                                             u'教育学',
                                             u'体育学',
                                             u'心理学',
                                             u'中国语言文学',
                                             u'外国语言文学',
                                             u'新闻传播学',
                                             u'广播电视学',
                                             u'广告学',
                                             u'编辑出版学'],
                            u'工学': [u'交通运输',
                                    u'海洋工程',
                                    u'生物工程'],
                            u'理学': [u'数学',
                                    u'物理',
                                    u'化学',
                                    u'生物科学'],
                            u'农学': [u'农学',
                                    u'园艺',
                                    u'园林']}

    level_three_dict_two = {u'机械': [u'机械制造',
                                    u'智能制造/机器人',
                                    u'数控',
                                    u'材料/模具',
                                    u'机电',
                                    u'汽车',
                                    u'职业基础课'],
                            u'电子电气': [u'通信',
                                      u'电力技术',
                                      u'电子信息',
                                      u'电气工程'],
                            u'建筑': [u'建筑专业',
                                    u'土建',
                                    u'水利',
                                    u'建筑工程管理',
                                    u'环境科学与工程'],
                            u'医学': [u'临床医学',
                                    u'护理助产',
                                    u'药学',
                                    u'口腔医学',
                                    u'医学技术',
                                    u'康复治疗技术',
                                    u'公共卫生'],
                            u'艺术/设计': [u'造型基础与艺术设计理论',
                                       u'数字媒体设计',
                                       u'工艺美术',
                                       u'工业设计',
                                       u'空间设计',
                                       u'视觉设计'],
                            u'外语/计算机': [u'外语',
                                        u'计算机',
                                        u'网络技术'],
                            u'管理学': [u'统计',
                                     u'财会',
                                     u'电子商务',
                                     u'市场营销',
                                     u'物流',
                                     u'旅游',
                                     u'公共管理'],
                            u'法律/经济': [u'法律实务',
                                       u'财政税务',
                                       u'金融',
                                       u'经济贸易'],
                            u'文学/教育': [u'新闻传播',
                                       u'教育',
                                       u'语言',
                                       u'文秘',
                                       u'体育'],
                            u'工学': [u'交通运输',
                                    u'食品药品',
                                    u'生物技术',
                                    u'化工技术'],
                            u'理学': [u'数学',
                                    u'物理',
                                    u'化学',
                                    u'生物学',
                                    u'资源勘查'],
                            u'农学': [u'农业',
                                    u'林业']}


    for index, item in enumerate(level_one_list):
        if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`) VALUES(%s, %s, %s)""", list1=(index + 1, item, 1)):
            print_log(item)

    index = get_last_id()

    for item in level_two_one_list:
        index += 1
        if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 2, 1)):
            print_log(item)

    index = get_last_id()

    for item in level_two_two_list:
        index += 1
        if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 2, 2)):
            print_log(item)

    index = get_last_id()

    for item in level_two_three_list:
        index += 1
        if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 2, 3)):
            print_log(item)

    index = get_last_id()

    for item in level_two_four_list:
        index += 1
        if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 2, 4)):
            print_log(item)

    for k, v in level_three_dict_one.items():
        current_parent_id = query_one(
            sql=u"""SELECT `id` FROM `category` WHERE name = %s AND parent_id = %s """, list1=(k, 1)).get('id')

        index = get_last_id()

        for item in v:
            index += 1
            if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 3, current_parent_id)):
                print_log(item)

    for k, v in level_three_dict_two.items():
        current_parent_id = query_one(
            sql=u"""SELECT `id` FROM `category` WHERE name = %s AND parent_id = %s """, list1=(k, 2)).get('id')

        index = get_last_id()
        for item in v:
            index += 1
            if save(sql=u"""INSERT INTO `category`(`id`, `name`, `level`, `parent_id`) VALUES(%s, %s, %s, %s)""" , list1=(index, item, 3, current_parent_id)):
                print_log(item)


def import_book():
    for item in xrange(111):
        name = 'Test__%s' % item
        number = 'Test__%s' % item
        author = 'Test__%s' % item
        price = random.randint(100,300)
        edit_number = 'Test__%s' % item
        publish_time = '%s-11-11' % (1800 + item)
        content = 'Test__%s' % item
        series_title = 'Test__%s' % item
        cover = 'Test__%s' % item
        directory = 'Test__%s' % item
        support_resource = random.choice([0, 1])
        author_introduction = 'Test__%s' % item
        characteristic = 'Test__%s' % item
        category_id = random.randint(1,187)

        if save(sql=u"""INSERT INTO `book`(`name`, `number`, `author`, `price`, `edit_number`, `publish_time`, `content`, `series_title`, `cover`, `directory`, `support_resource`, `author_introduction`, `characteristic`, `category_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """, list1=(name, number, author, price, edit_number, publish_time, content, series_title, cover, directory, support_resource, author_introduction, characteristic, category_id, )):
            print_log(name)


def main():
    import_category()
    # import_book()

if __name__ == '__main__':
    main()
