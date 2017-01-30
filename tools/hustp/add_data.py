# -*- coding: utf-8 -*-
from mysql import query, query_one, save


def get_last_id():
    return query_one(sql=u"""SELECT `id` FROM `category` ORDER BY `id` DESC LIMIT 0,1 """).get('id')


def print_log(item):
    print "INSERT < %s > SUCCESS!" % item


def import_category():
    level_one_list = [u'本科', u'高职', u'研究生', u'中职']
    level_two_one_list = [u'机械', u'电子电气', u'建筑', u'医学', u'艺术/设计', u'外语/计算机/网络',
                          u'管理学', u'法学/经济', u'工学', u'理学', u'文学/哲学/历史/教育', u'农学', u'公共课']
    level_two_two_list = [u'机械', u'电子电气', u'建筑', u'医学', u'艺术/设计', u'外语/计算机/网络',
                          u'管理学', u'法律/经济', u'工学', u'理学', u'文学/教育', u'农学', u'公共课']
    level_two_three_list = [u'机械', u'电工电子', u'外语', u'人文社科', u'其它']

    level_two_four_list = [u'旅游与饭店管理', u'汽车类',
                           u'计算机', u'机电', u'模具', u'数控', u'化学', u'其它']
    level_three_dict_one = {u'机械': [u'材料类', u'冶金工程', u'金属材料工程', u'无机非金属材料工程', u'高分子材料与工程', u'材料科学与工程', u'机械类', u'机械设计制造及其自动化', u'材料成型及控制工程', u'工业设计', u'过程装备与控制工程', u'机械工程及自动化', u'仪器仪表类', u'测控技术与仪器', u'能源动力类', u'热能与动力工程', u'核工程与核技术'],
                            u'电子电气': [u'电气信息', u'电气工程及其自动化', u'自动化', u'电子信息工程', u'通信工程', u'计算机科学与技术', u'电子科学与技术', u'智能电网信息工程', u'光源与照明', u'电气工程与智能控制', u'微电子科学与工程', u'光电信息科学与工程'],
                            u'建筑': [u'土建', u'建筑专业', u'风景园林', u'土木专业', u'建筑环境与设备工程', u'环境设计', u'室内设计', u'环境科学与工程', u'城市规划', u'水利类', u'测绘类', u'环境工程', u'安全工程'],
                            u'医学': [u'基础医学', u'预防医学', u'临床医学与医学技术类', u'临床医学', u'麻醉学', u'医学影像学', u'医学检验', u'口腔医学', u'中医学', u'针灸推拿学', u'法医学', u'护理学', u'药学', u'中药学', u'药物制剂'],
                            u'艺术/设计': [u'数字媒体设计', u'造型基础', u'工艺美术', u'工业设计', u'空间设计', u'视觉设计', u'艺术设计', u'视觉传达设计', u'产品设计', u'服装与服饰设计', u'公共艺术', u'音乐类', u'绘画/美术', u'摄影', u'舞蹈/表演', u'动画', u'播音与主持艺术'],
                            u'外语/计算机/网络': [u'大学英语', u'高等教育英语', u'高校英语专业', u'英语考试', u'专业英语', u'日语/法语/俄语', u'计算机基础', u'计算机硬件设备及其维修', u'操作系统', u'数据库语言与编程', u'网络与计算机及其安全', u'图形图象处理及计算机辅助设计', u'多媒体', u'网页设计及制作', u'软件工程/软件技术', u'人工智能', u'网络技术'],
                            u'管理学': [u'管理科学与工程类', u'信息管理与信息系统', u'工业工程', u'工程管理', u'工商管理类', u'市场营销', u'会计学', u'财务管理', u'人力资源管理', u'旅游管理', u'物流管理', u'房地产经营管理', u'公共管理类', u'行政管理', u'公共事业管理', u'劳动与社会保障', u'电子商务'],
                            u'法学/经济': [u'法学类', u'法理．宪法．行政法．法律史', u'诉讼法', u'民商法', u'经济法', u'刑法', u'国际法', u'司考与法硕考试用书', u'社会学类', u'政治学类', u'监狱培训', u'经济学', u'国际经贸', u'财政学', u'金融学'],
                            u'工学': [u'地矿类', u'化工与制药类', u'交通运输类', u'轮机工程', u'海洋工程类', u'纺织类', u'工程力学类', u'生物工程类', u'农业工程学', u'消防工程', u'生物医学工程'],
                            u'理学': [u'数学与应用数学', u'信息与计算科学', u'物理学类', u'物理学', u'应用物理学', u'核物理', u'化学类', u'天文学类', u'地理科学类', u'大气科学类', u'海洋科学类', u'地球物理学类', u'地质学类', u'生物科学类', u'心理学类', u'统计学类'],
                            u'文学/哲学/历史/教育': [u'哲学', u'宗教学', u'历史学', u'教育学类', u'学前教育', u'体育学类', u'心理学', u'中国语言文学类', u'外国语言文学类', u'传播学', u'新闻学', u'广播电视学', u'广告学', u'编辑出版学'],
                            u'农学': [u'植物生产类', u'农学', u'园艺', u'植物保护', u'林学', u'环境生态类', u'园林', u'动物科学', u'水产类'],
                            u'公共课': [u'全部']}

    level_three_dict_two = {u'机械': [u'能源动力类', u'热能与动力工程', u'数控/自动化', u'机械设计', u'机电', u'材料/模具', u'汽车类', u'装备制造', u'智能制造/机器人'],
                            u'电子电气': [u'电力技术', u'通信', u'电子信息', u'电气工程'],
                            u'建筑': [u'建筑设计', u'土建类', u'环境科学与工程', u'环境保护', u'安全类', u'建筑工程管理', u'水利类'],
                            u'医学': [u'临床类', u'护理类', u'药学类', u'医学技术', u'康复类', u'公共卫生', u'人口与计划生育', u'健康管理'],
                            u'艺术/设计': [u'数字媒体设计', u'造型基础', u'工艺美术', u'工业设计', u'空间设计', u'视觉设计', u'艺术设计', u'视觉传达设计', u'产品设计', u'服装与服饰设计', u'公共艺术', u'音乐类', u'绘画/美术', u'摄影', u'舞蹈/表演', u'动画', u'播音与主持艺术'], u'外语/计算机/网络': [u'外语', u'计算机', u'网络'],
                            u'管理学': [u'公共服务类', u'统计类', u'财会类', u'市场营销', u'物流类', u'旅游类', u'电子商务', u'公共管理类', u'公共事业类'],
                            u'法律/经济': [u'公安管理', u'公安指挥', u'公安技术', u'侦查类', u'法律实务', u'司法技术', u'财政税务', u'金融', u'经济贸易'],
                            u'工学': [u'地矿类', '交通运输类', '纺织类', '邮政', '粮食', '食品药品', '生物技术', '化工技术', '轻化工', '包装', '印刷'],
                            u'理学': [u'数学', u'物理', u'地质学', u'生物学', u'资源勘查', u'测绘地理', u'气象类'],
                            u'文学/教育': [u'新闻传播类', u'教育', u'语言', u'文秘', u'体育'],
                            u'农学': [u'林业', u'畜牧业', u'渔业', u'农业'],
                            u'公共课': [u'全部']}

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
    for item in xrange(6):
        id = item + 1
        name = 'Test_%s' % item
        number = 'Test_%s' % item
        subject = 'Test_%s' % item
        author = 'Test_%s' % item
        price = item
        edit_number = 'Test_%s' % item
        publish_time = 'Test_%s' % item
        content = 'Test_%s' % item
        series_title = 'Test_%s' % item
        cover = 'Test_%s' % item
        directory = 'Test_%s' % item
        support_resource = True
        author_introduction = 'Test_%s' % item
        gradation = 'Test_%s' % item
        characteristic = 'Test_%s' % item
        major = item + 1

        if save(sql=u"""INSERT INTO `book`(`id`, `name`, `number`, `subject`, `author`, `price`, `edit_number`, `publish_time`, `content`, `series_title`, `cover`, `directory`, `support_resource`, `author_introduction`, `gradation`, `characteristic`, `major_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """, list1=(id, name, number, subject, author, price, edit_number, publish_time, content, series_title, cover, directory, support_resource, author_introduction, gradation, characteristic, major,)):
            print_log(name)


def main():
    import_category()
    import_book()

if __name__ == '__main__':
    main()
