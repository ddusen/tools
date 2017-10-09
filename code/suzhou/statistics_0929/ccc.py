# -*- coding: utf-8 -*-
import xlwt
from mysql import query, query_one, save

# 3c 产品编码
ccc_dict = {'2d17': u'安全玻璃',
            '1431': u'车的其他零部件和附件',
            '6ba3': u'电焊机',
            '171f': u'电线电缆',
            '6c5f': u'额定电压450/750KV及以下橡皮绝缘电线电缆',
            'c3cd': u'额定电压450/750V及以下聚氯乙烯绝缘电线电缆',
            '5151': u'交流额定电压3kV及以下铁路机车车辆用电线电缆',
            'f5f0': u'手持式电动工具',
            '6498': u'小功率电动机',
            '21e4': u'吸油烟机',
            '07a8': u'室内加热器',
            '1c56': u'家用电冰箱和食品冷冻箱',
            'a113': u'家用电动洗衣机',
            'ec23': u'液体加热器和冷热饮水机',
            '570f': u'空气压缩机',
            '06fa': u'厨房机械',
            'e237': u'电烤箱',
            '903e': u'电热水器',
            'bd65': u'电熨斗',
            '31b0': u'电磁灶',
            '4d50': u'电风扇',
            'ca97': u'电饭煲',
            'fa00': u'皮肤和毛发护理器具',
            '6ba9': u'吸尘器',
            'bea6': u'空调器',
            '00a9': u'机动车及其配件',
            'aadf': u'机动车灯具',
            '2035': u'汽车制动软管总成',
            '9e3e': u'机动车成年乘员用安全带',
            'a56a': u'消防水带',
            '5f24': u'干粉灭火器',
            'ea25': u'防火门',
            '7307': u'防爆、消防产品',
            '197a': u'消防应急照明产品',
            'f21b': u'灯及灯具',
            '6e4a': u'普通照明用自镇流荧光灯',
            '7393': u'电信终端设备',
            'e8ac': u'无绳电话终端',
            '3fa4': u'移动用户终端',
            '15fe': u'调制解调器',
            'f7a3': u'固定电话终端',
            '3f82': u'耦合器',
            'fd8b': u'家用和类用途固定式电气装置电器附件外壳',
            '525e': u'家用和类用途固定式电气装置的开关',
            '044f': u'小型熔断器的管状熔断体',
            '611f': u'插头插座',
            '92bf': u'混凝土添加剂',
            '249c': u'溶剂型木器涂料',
            '39ee': u'陶瓷砖',
            'af67': u'液晶显示器',
            'e55a': u'电视接收机',
            'd8ff': u'DVD视盘机',
            '6871': u'投影机',
            '4d88': u'便携式音箱',
            'f337': u'音频、视频设备',
            '3f1c': u'监视器',
            'cadc': u'组合音响',
            'ea1c': u'低压电器、开关',
            '5b3b': u'低压成套开关设备',
            'a3a8': u'其他开关',
            '12e6': u'其他电路保护装置',
            'a96f': u'断路器',
            'bc7a': u'漏电保护器',
            'af72': u'信息技术设备',
            '6c77': u'与计算机相连的打印设备',
            'b3ab': u'笔记本电脑',
            'e98a': u'计算机',
            '9c61': u'税控收款机',
            '636e': u'服务器',
            '1f44': u'手持式电子信息器具',
            'a471': u'电源适配器',
            'a240': u'儿童玩具',
            'c392': u'机动车儿童乘员用约束系统',
            '5eec': u'童车',
            '8d23': u'植物保护机械',
            '32cf': u'点型感烟火灾探测器',
            '7ad8': u'汽车防盗报警系统',
            '53e6': u'防盗报警控制器',
            '578b': u'安全防范产品',
            'caf6': u'家用和类似用途的电器'}


def handle_data():
    data = []
    for k,v in ccc_dict.items():
        base_product_id = query_one(sql=u'SELECT `id` FROM `base_product` WHERE `code`=%s', list1=(k, )).get('id')
        enterprise_number = len(query(sql=u'SELECT DISTINCT `a19` FROM `base_chinacompulsorycertification` WHERE `a4` LIKE %s OR `a5` LIKE %s OR `a11` LIKE %s', list1=("%%%s%%" % v, "%%%s%%" % v, "%%%s%%" % v, )))
        ccc_certificate_number = query_one(sql=u'SELECT COUNT(*) FROM `base_chinacompulsorycertification` WHERE `a4` LIKE %s OR `a5` LIKE %s OR `a11` LIKE %s', list1=("%%%s%%" % v, "%%%s%%" % v, "%%%s%%" % v, )).get('COUNT(*)')

        base_samplingproduct_id = query_one(sql=u'SELECT `id` FROM `base_samplingproduct` WHERE `code`=%s', list1=(k, )).get('id')
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
    file.save('/home/sdu/Project/tools/code/suzhou/statistics_0929/2017监督抽查统计0929.xls')


def main():
    export_excel(handle_data())


if __name__ == '__main__':
    print main()
