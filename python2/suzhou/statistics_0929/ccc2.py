# -*- coding: utf-8 -*-
import xlwt
from mysql import query, query_one, save

# 3c 产品编码
ccc_tuple = (u'电线电缆',
            u'电线组件',
            u'交流额定电压3kV及以下铁路机车车辆用电线电缆',
            u'额定电压450/750V及以下橡皮绝缘电线电缆',
            u'额定电压450/750V及以下聚氯乙烯绝缘电线电缆',
            u'电路开关及保护或连接用电器装置',
            u'插头插座(家用和类似用途、工业用)',
            u'家用和类似用途固定式电气装置的开关',
            u'器具耦合器（家用和类似用途、工业用）',
            u'热熔断体',
            u'家用和类似用途固定式电气装置电器附件外壳',
            u'小型熔断器的管状熔断体',
            u'低压电器',
            u'漏电保护器',
            u'断路器',
            u'熔断器',
            u'低压开关（隔离器、隔离开关、熔断器组合电器）',
            u'其他电路保护装置',
            u'继电器',
            u'其他开关',
            u'其他装置',
            u'低压成套开关设备',
            u'小功率电动机',
            u'电动工具',
            u'电钻',
            u'电动螺丝刀和冲击扳手',
            u'电动砂轮机',
            u'砂光机',
            u'圆锯',
            u'电锤',
            u'不易燃液体电喷枪',
            u'电剪刀',
            u'攻丝机',
            u'往复锯',
            u'插入式混凝土振动器',
            u'电链锯',
            u'电刨',
            u'电动修枝剪',
            u'电木铣和修边机',
            u'电动石材切割机',
            u'电焊机',
            u'小型交流弧焊机',
            u'交流弧焊机',
            u'直流弧焊机',
            u'TIG弧焊机',
            u'MIG/MAG弧焊机',
            u'埋弧焊机',
            u'等离子弧切割机',
            u'等离子弧焊机',
            u'弧焊变压器防触电装置',
            u'焊接电缆耦合装置',
            u'电阻焊机',
            u'送丝装置',
            u'TIG焊焊炬',
            u'MIG/MAG焊焊枪',
            u'电焊钳',
            u'家用和类似用途设备',
            u'家用电冰箱和食品冷冻箱',
            u'电风扇',
            u'空调器',
            u'电动机－压缩机',
            u'家用电动洗衣机',
            u'电热水器',
            u'室内加热器',
            u'真空吸尘器',
            u'皮肤和毛发护理器具',
            u'电熨斗',
            u'电磁灶',
            u'电烤箱',
            u'电动食品加工器具',
            u'微波炉',
            u'电灶、灶台、烤炉和类似器具',
            u'吸油烟机',
            u'液体加热器和冷热饮水机',
            u'电饭锅',
            u'音视频设备',
            u'总输出功率在500W（有效值）以下的单扬声器和多扬声器有源音箱',
            u'音频功率放大器',
            u'各种广播波段的调谐接收机、收音机',
            u'各类载体形式的音视频录制播放及处理设备',
            u'以上四种设备的组合',
            u'音视频设备配套的电源适配器',
            u'各种成像方式的彩色电视接收机',
            u'监视器',
            u'显像（示）管',
            u'录像机',
            u'电子琴',
            u'天线放大器',
            u'微型计算机',
            u'便携式计算机',
            u'与计算机连用的显示设备',
            u'与计算机相连的打印设备',
            u'多用途打印复印机',
            u'扫描仪',
            u'计算机内置电源及电源适配器充电器',
            u'电脑游戏机',
            u'学习机',
            u'复印机',
            u'服务器',
            u'照明电器',
            u'灯具',
            u'镇流器',
            u'机动车辆及安全附件',
            u'汽车',
            u'摩托车',
            u'消防车',
            u'摩托车发动机',
            u'汽车安全带',
            u'机动车喇叭',
            u'机动车回复反射器',
            u'机动车制动软管',
            u'机动车外部照明及光信号装置',
            u'机动车辆间接视野装置',
            u'汽车内饰件',
            u'汽车门锁及门保持件',
            u'汽车燃油箱',
            u'汽车座椅及座椅头枕',
            u'汽车行驶记录仪',
            u'车身反光标识',
            u'轿车轮胎',
            u'载重汽车轮胎',
            u'摩托车轮胎',
            u'汽车安全玻璃',
            u'建筑安全玻璃',
            u'铁道车辆安全玻璃',
            u'农机产品',
            u'植物保护机械',
            u'轮式拖拉机',
            u'电信终端设备',
            u'调制解调器',
            u'传真机',
            u'固定电话终端及电话机附加装置',
            u'无绳电话终端',
            u'集团电话',
            u'移动用户终端',
            u'ISDN终端',
            u'数据终端',
            u'多媒体终端',
            u'消防产品',
            u'火灾报警产品',
            u'消防水带',
            u'喷水灭火产品',
            u'灭火剂',
            u'建筑耐火构件',
            u'泡沫灭火设备产品',
            u'消防装备产品',
            u'火灾防护产品',
            u'灭火器',
            u'消防给水设备产品',
            u'气体灭火设备产品',
            u'干粉灭火设备产品',
            u'消防防烟排烟设备产品',
            u'避难逃生产品',
            u'消防通信产品',
            u'安全防范产品',
            u'入侵探测器',
            u'防盗报警控制器',
            u'汽车防盗报警系统',
            u'防盗保险柜',
            u'防盗保险箱',
            u'无线局域网产品',
            u'无线局域网产品',
            u'装饰装修产品',
            u'溶剂型木器涂料',
            u'瓷质砖',
            u'混凝土防冻剂',
            u'儿童用品',
            u'童车类产品',
            u'电玩具类产品',
            u'塑胶玩具类产品',
            u'金属玩具类产品',
            u'弹射玩具类产品',
            u'娃娃玩具类产品',
            u'机动车儿童乘员用约束系统')


def handle_data():
    data = []
    for v in ccc_tuple:
        base_product_id = query_one(sql=u'SELECT `id` FROM `base_product` WHERE `name`=%s', list1=(v, ))
        base_product_id = 1 if not base_product_id else base_product_id.get('id')
        enterprise_number = len(query(sql=u'SELECT DISTINCT `a19` FROM `base_chinacompulsorycertification` WHERE `a4` LIKE %s OR `a5` LIKE %s OR `a11` LIKE %s', list1=("%%%s%%" % v, "%%%s%%" % v, "%%%s%%" % v, )))
        ccc_certificate_number = query_one(sql=u'SELECT COUNT(*) FROM `base_chinacompulsorycertification` WHERE `a4` LIKE %s OR `a5` LIKE %s OR `a11` LIKE %s', list1=("%%%s%%" % v, "%%%s%%" % v, "%%%s%%" % v, )).get('COUNT(*)')

        base_samplingproduct_id = query_one(sql=u'SELECT `id` FROM `base_samplingproduct` WHERE `name`=%s', list1=(v, ))
        base_samplingproduct_id = 1 if not base_samplingproduct_id else base_samplingproduct_id.get('id')
        base_samplingproductenterprise_queryset = query(sql=u'SELECT `sampling_id` FROM `base_samplingproductenterprise` WHERE `sampling_product_id` = %s', list1=(base_samplingproduct_id, ))
        base_sampling_ids = map(lambda x : x.values()[0], base_samplingproductenterprise_queryset)
        base_sampling_ids_str = ', '.join(list(map(lambda x: '%s', base_sampling_ids)))

        patch_2017 = query_one(sql=u'SELECT COUNT(*) FROM `base_sampling` WHERE `check_year` = "2017" AND `id` IN (%s)', list1=(base_sampling_ids_str, )).get('COUNT(*)')
        patch_2017_2 = 1 if patch_2017 == 0 else patch_2017
        enterprise_number_2 = 1 if enterprise_number == 0 else enterprise_number
        inspect_money = u'空'
        inspect_proportion = str(( patch_2017_2 / enterprise_number_2 ) * 100) + '%'

        unit_price = u'空'

        patch_2017_qualified = query_one(sql=u'SELECT COUNT(*) FROM `base_sampling` WHERE `check_year` = "2017" AND `check_result` = "合格" AND `id` IN (%s)', list1=(base_sampling_ids_str, )).get('COUNT(*)')
        patch_2017_qualified = 1 if patch_2017_qualified == 0 else patch_2017_qualified 

        patch_2017_qualified_rate = str(( patch_2017_qualified / patch_2017_2)* 100) + '%'

        patch_2016 = query_one(sql=u'SELECT COUNT(*) FROM `base_sampling` WHERE `check_year` = "2016" AND `id` IN (%s)', list1=(base_sampling_ids_str, )).get('COUNT(*)')
        patch_2016 = 1 if patch_2016 == 0 else patch_2016
        patch_2016_qualified = query_one(sql=u'SELECT COUNT(*) FROM `base_sampling` WHERE `check_year` = "2016" AND `check_result` = "合格" AND `id` IN (%s)', list1=(base_sampling_ids_str, )).get('COUNT(*)')
        patch_2016_qualified = 1 if patch_2016_qualified == 0 else patch_2016_qualified

        patch_2016_qualified_rate = str((patch_2016_qualified / patch_2016)*100) +'%'

        data.append((v, enterprise_number, ccc_certificate_number, patch_2017, inspect_money, inspect_proportion, unit_price, patch_2017_qualified_rate, patch_2016_qualified_rate, ))

    return data


def export_excel(data):
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet(u'强制认证', cell_overwrite_ok=True)

    for index, d in enumerate(data):
            table.write(index, 0, index + 1)
            table.write(index, 1, d[0])
            table.write(index, 2, d[1])
            table.write(index, 3, d[2])
            table.write(index, 4, d[3])
            table.write(index, 5, d[4])
            table.write(index, 6, d[5])
            table.write(index, 7, d[6])
            table.write(index, 8, d[7])
            table.write(index, 9, d[8])

    # 保存文件
    file.save('/home/sdu/Project/tools/code/suzhou/statistics_0929/2017监督抽查统计1009.xls')


def main():
    export_excel(handle_data())


if __name__ == '__main__':
    print main()
