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
    for item in xrange(30):
        name = 'Test__%s' % item
        number = 'Test__%s' % item
        author = 'Test__%s' % item
        price = random.randint(100, 300)
        edit_number = 'Test__%s' % item
        publish_time = '%s-11-11' % (1800 + item)
        content = 'Test__%s' % item
        series_title = 'Test__%s' % item
        cover = 'Test__%s' % item
        directory = 'Test__%s' % item
        support_resource = random.choice([0, 1])
        author_introduction = 'Test__%s' % item
        characteristic = 'Test__%s' % item

        if save(sql=u"""INSERT INTO `book`(`name`, `number`, `author`, `price`, `edit_number`, `publish_time`, `content`, `series_title`, `cover`, `directory`, `support_resource`, `author_introduction`, `characteristic`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """, list1=(name, number, author, price, edit_number, publish_time, content, series_title, cover, directory, support_resource, author_introduction, characteristic,)):
            print_log(name)


def add_note():
    if save(sql=u"""INSERT INTO `note` VALUES (1,'<p>空</p>','<p>空</p>','<p>空</p>','<p>空</p>','<p>空</p>','<p>空</p>')"""):
        print_log('note')


def add_auth_group():
    if save(sql=u"""INSERT INTO `auth_group` VALUES(1,'超级用户')"""):
        print_log('超级用户')

    if save(sql=u"""INSERT INTO `auth_group` VALUES(2,'图书管理')"""):
        print_log('图书管理')


def add_auth_group_permissions():
    if save(sql=u"""INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,32),(32,1,34),(33,1,35),(34,1,36),(35,2,19),(36,2,20),(37,2,21)"""):
        print_log('auth_group_permissions')


def add_auth_permission():
    if save(sql=u"""INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add book',7,'add_book'),(20,'Can change book',7,'change_book'),(21,'Can delete book',7,'delete_book'),(22,'Can add category',8,'add_category'),(23,'Can change category',8,'change_category'),(24,'Can delete category',8,'delete_category'),(25,'Can add sample apply',9,'add_sampleapply'),(26,'Can change sample apply',9,'change_sampleapply'),(27,'Can delete sample apply',9,'delete_sampleapply'),(28,'Can add courseware apply',10,'add_coursewareapply'),(29,'Can change courseware apply',10,'change_coursewareapply'),(30,'Can delete courseware apply',10,'delete_coursewareapply'),(31,'Can add note',11,'add_note'),(32,'Can change note',11,'change_note'),(33,'Can delete note',11,'delete_note'),(34,'Can add teacher',12,'add_teacher'),(35,'Can change teacher',12,'change_teacher'),(36,'Can delete teacher',12,'delete_teacher')"""):
        print_log('auth_permission')


def add_auth_user():
    if save(sql=u"""INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$24000$Ktol7VpCMLM0$m83AXfaOj31yuL3JxNRqKb6Exr0pmvKl8oLjTSPSzA8=',NULL,0,'fxdj','杜鹃','','',1,1,'2017-02-27 05:43:00'),(3,'pbkdf2_sha256$24000$dImgs04ivtgs$U7P5dL+iQq6rbZm4jJPt1TN6Yx0gCcnbkcU4k+ugV5s=',NULL,0,'fxdx','杜雄','','',1,1,'2017-02-27 05:44:00'),(4,'pbkdf2_sha256$24000$tMAZ4xxBmxup$qnoDv5/DSgMnw4I+h2ROrg3Ch2xJ3XRkwCzfI1TINF8=',NULL,0,'fxhq','黄琪','','',1,1,'2017-02-27 05:44:00'),(5,'pbkdf2_sha256$24000$ndRC1SNqPNrq$wQJAsOxo+kTyBt5sQkdyfS8PoRvo/CjzNTpdBqHypBM=',NULL,0,'fxly','李永','','',1,1,'2017-02-27 05:45:00'),(6,'pbkdf2_sha256$24000$s9lzlwXvR7gN$F+PAEZJpltZQ500mUIN+PZGfNGus1YDvwEjgVCRXVCw=',NULL,0,'fxnyw','聂亚文','','',1,1,'2017-02-27 05:46:00'),(7,'pbkdf2_sha256$24000$RokVxi0Q8TFM$o7CFi9r6D5YPVVrgg3UTTSFeMbWkJS4u1Qz2PuQoMcA=','2017-02-27 05:47:42',0,'fxxjs','徐建生','','',1,1,'2017-02-27 05:46:00'),(8,'pbkdf2_sha256$24000$RXIii1HFos2Y$SxGl8phAZKoogO9L2XkvPAQp+ONX/7jgQzgo9jZeEHY=',NULL,0,'jiaocaifuwu','公共','','',1,1,'2017-02-27 05:47:00')"""):
        print_log('auth_user')


def add_auth_user_groups():
    if save(sql=u"""INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,2),(3,4,2),(4,5,2),(5,6,2),(6,7,1),(7,8,2)"""):
        print_log('auth_user_groups')


def add_category():
    if save(sql=u"""INSERT INTO `category` VALUES (1,'本科',1,NULL),(2,'高职',1,NULL),(3,'研究生',1,NULL),(4,'中职',1,NULL),(5,'机械',2,1),(6,'电子电气',2,1),(7,'建筑',2,1),(8,'医学',2,1),(9,'艺术/设计',2,1),(10,'外语/计算机',2,1),(11,'管理学',2,1),(12,'法律/经济/社会/政治',2,1),(13,'文学/哲学/历史/教育',2,1),(14,'工学',2,1),(15,'理学',2,1),(16,'农学',2,1),(17,'公共课',2,1),(18,'机械',2,2),(19,'电子电气',2,2),(20,'建筑',2,2),(21,'医学',2,2),(22,'艺术/设计',2,2),(23,'外语/计算机',2,2),(24,'管理学',2,2),(25,'法律/经济',2,2),(26,'文学/教育',2,2),(27,'工学',2,2),(28,'理学',2,2),(29,'农学',2,2),(30,'公共课',2,2),(31,'机械',2,3),(32,'电工电子',2,3),(33,'外语',2,3),(34,'人文社科',2,3),(35,'其它',2,3),(36,'旅游',2,4),(37,'汽车',2,4),(38,'计算机',2,4),(39,'机电',2,4),(40,'模具',2,4),(41,'数控',2,4),(42,'医学/化学',2,4),(43,'其他',2,4),(44,'法学',3,12),(45,'社会学',3,12),(46,'政治学',3,12),(47,'经济学',3,12),(48,'国际经贸',3,12),(49,'财政学',3,12),(50,'金融学',3,12),(51,'监狱培训',3,12),(52,'工商管理',3,11),(53,'市场营销',3,11),(54,'会计学',3,11),(55,'电子商务',3,11),(56,'财务管理',3,11),(57,'人力资源管理',3,11),(58,'旅游管理',3,11),(59,'物流管理',3,11),(60,'房地产经营管理',3,11),(61,'公共管理',3,11),(62,'行政管理',3,11),(63,'信息管理与信息系统',3,11),(64,'交通运输',3,14),(65,'海洋工程',3,14),(66,'生物工程',3,14),(67,'基础医学',3,8),(68,'临床医学与医学技术',3,8),(69,'医学检验',3,8),(70,'中医学',3,8),(71,'护理学',3,8),(72,'药学',3,8),(73,'医学人文',3,8),(74,'通信工程',3,6),(75,'电子信息工程',3,6),(76,'微电子科学与工程',3,6),(77,'光电信息科学与工程',3,6),(78,'电气工程及其自动化',3,6),(79,'电子科学与技术',3,6),(80,'自动化',3,6),(81,'材料及工程',3,5),(82,'机械设计制造及其自动化',3,5),(83,'机械工程及自动化',3,5),(84,'测控技术与仪器',3,5),(85,'能源动力',3,5),(86,'工程力学',3,5),(87,'学科基础课',3,5),(88,'土木专业',3,7),(89,'建筑学',3,7),(90,'风景园林',3,7),(91,'城市规划',3,7),(92,'建筑环境与设备工程',3,7),(93,'环境设计',3,7),(94,'环境科学与工程',3,7),(95,'农学',3,16),(96,'园艺',3,16),(97,'园林',3,16),(98,'数学',3,15),(99,'物理',3,15),(100,'化学',3,15),(101,'生物科学',3,15),(102,'大学英语',3,10),(103,'专业英语',3,10),(104,'英语考试',3,10),(105,'日语/法语/俄语',3,10),(106,'计算机基础',3,10),(107,'计算机科学与技术',3,10),(108,'软件工程/软件技术',3,10),(109,'网络安全',3,10),(110,'基础课与艺术设计理论',3,9),(111,'动漫设计',3,9),(112,'音乐',3,9),(113,'产品设计',3,9),(114,'环境艺术设计',3,9),(115,'视觉传达设计',3,9),(116,'哲学',3,13),(117,'历史学',3,13),(118,'教育学',3,13),(119,'体育学',3,13),(120,'心理学',3,13),(121,'中国语言文学',3,13),(122,'外国语言文学',3,13),(123,'新闻传播学',3,13),(124,'广播电视学',3,13),(125,'广告学',3,13),(126,'编辑出版学',3,13),(127,'新闻传播',3,26),(128,'教育',3,26),(129,'语言',3,26),(130,'文秘',3,26),(131,'体育',3,26),(132,'法律实务',3,25),(133,'财政税务',3,25),(134,'金融',3,25),(135,'经济贸易',3,25),(136,'统计',3,24),(137,'财会',3,24),(138,'电子商务',3,24),(139,'市场营销',3,24),(140,'物流',3,24),(141,'旅游',3,24),(142,'公共管理',3,24),(143,'交通运输',3,27),(144,'食品药品',3,27),(145,'生物技术',3,27),(146,'化工技术',3,27),(147,'临床医学',3,21),(148,'护理助产',3,21),(149,'药学',3,21),(150,'口腔医学',3,21),(151,'医学技术',3,21),(152,'康复治疗技术',3,21),(153,'公共卫生',3,21),(154,'通信',3,19),(155,'电力技术',3,19),(156,'电子信息',3,19),(157,'电气工程',3,19),(158,'机械制造',3,18),(159,'智能制造/机器人',3,18),(160,'数控',3,18),(161,'材料/模具',3,18),(162,'机电',3,18),(163,'汽车',3,18),(164,'职业基础课',3,18),(165,'建筑专业',3,20),(166,'土建',3,20),(167,'水利',3,20),(168,'建筑工程管理',3,20),(169,'环境科学与工程',3,20),(170,'农业',3,29),(171,'林业',3,29),(172,'数学',3,28),(173,'物理',3,28),(174,'化学',3,28),(175,'生物学',3,28),(176,'资源勘查',3,28),(177,'外语',3,23),(178,'计算机',3,23),(179,'网络技术',3,23),(180,'造型基础与艺术设计理论',3,22),(181,'数字媒体设计',3,22),(182,'工艺美术',3,22),(183,'工业设计',3,22),(184,'空间设计',3,22),(185,'视觉设计',3,22)"""):
        print_log('category')


def add_django_content_type():
    if save(sql=u"""INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'book','book'),(8,'book','category'),(10,'book','coursewareapply'),(11,'book','note'),(9,'book','sampleapply'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(12,'teacher','teacher')"""):
        print_log('django_content_type')


def add_django_session():
    if save(sql=u"""INSERT INTO `django_session` VALUES ('okaxy750gf95qtojwrc3x2e91dexdt3z','MGI1MWJkMjdhMmVlNDM2MGFkZjMxYTU1NzRjZWIyMTg2YzUwYTcxNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjJmMmExNDZjNzZhNzg0MWZiODlhZDA5ZjBlOTlhNTAzODc3MGViODgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2017-03-13 05:47:42')"""):
        print_log('django_session')


def main():
    # import_category()
    # import_book()
    add_note()
    add_auth_group()
    add_auth_group_permissions()
    add_auth_permission()
    add_auth_user()
    add_auth_user_groups()
    add_category()
    add_django_content_type()
    add_django_session()


if __name__ == '__main__':
    main()
