# -*- coding: utf-8 -*-
import xlwt
from mysql import query, query_one, save

# license 产品编码
license_dict = {
    '78d1': u'泵',
    'df93': u'电力金具',
    'dea8': u'电力整流器',
    '7223': u'电热毯',
    '171f': u'电线电缆',
    '258e': u'防爆电气',
    '4c61': u'防喷器及防喷器控制装置',
    '78c1': u'防伪技术产品',
    '2921': u'非金属密封制品',
    '0a9c': u'钢筋混凝土用热轧钢筋',
    '9ece': u'钢丝绳',
    'cc6c': u'港口装卸机械',
    'ea80': u'工业硝酸',
    'f18d': u'公路桥梁支座',
    '1867': u'广播通信铁塔及桅杆',
    '123b': u'化肥、农药及农用塑料制品',
    '2034': u'机动车制动液',
    '5c4e': u'机动脱粒机',
    '567e': u'机械密封',
    '9452': u'集成电路卡及集成电路卡读写机',
    '1251': u'建筑防水卷材',
    '723a': u'建筑钢管脚手架扣件',
    '1ff9': u'建筑卷扬机',
    '42e7': u'建筑外窗',
    '570f': u'空气压缩机',
    'f7b5': u'铝合金建筑型材',
    '2404': u'氯碱',
    '5262': u'棉花加工机械',
    '380c': u'摩擦材料',
    'ad9c': u'摩托车乘员头盔',
    'f434': u'耐火材料',
    'f434': u'耐火材料',
    'e349': u'内燃机',
    '7b3c': u'农药',
    '30b1': u'铅酸蓄电池',
    'fbf7': u'轻小型起重运输设备',
    '4281': u'燃气器具',
    '2994': u'人民币鉴别仪',
    'dd16': u'人造板',
    '5197': u'砂轮',
    'cab5': u'食品相关产品',
    '8e9b': u'输电线路铁塔',
    '8475': u'输水管',
    '7000': u'水工金属结构',
    '64c7': u'水泥',
    '668e': u'水文仪器',
    '9c61': u'税控收款机',
    '9c61': u'税控收款机',
    '222e': u'钛及钛合金加工产品',
    '99c5': u'碳化钙',
    '58fd': u'特种劳动防护用品',
    '18c1': u'天然气、石油钻采设备',
    'b484': u'调度绞车',
    '8e53': u'铜及铜合金管材',
    '8ea1': u'危险化学品包装物',
    '1721': u'危险化学品及危险化学品包装、容器',
    'f0b5': u'危险化学品石油',
    '278f': u'危险化学品涂料',
    'a023': u'危险化学品无机类',
    'a023': u'危险化学品无机类',
    'a023': u'危险化学品无机类',
    '75bf': u'危险化学品有机类',
    '75bf': u'危险化学品有机类',
    'ed96': u'卫星电视广播地面接收设备',
    'a07f': u'无线广播电视发射设备',
    'a773': u'橡胶及塑料制品',
    '1855': u'岩土工程仪器',
    'ecfc': u'眼镜',
    'd00a': u'预应力混凝土铁路桥简支梁',
    'cd92': u'预应力混凝土用钢材',
    '210b': u'预应力混凝土枕',
    '8460': u'制冷设备',
    'a56f': u'轴承',
    '9bdd': u'助力车',
    'faa7': u'钻井悬吊工具',
}

def handle_data():
    data = []
    for k,v in license_dict.items():
        base_product_id = query_one(sql=u'SELECT `id` FROM `base_product` WHERE `code`=%s', list1=(k, )).get('id')

        base_licenseproduct_id = query_one(sql=u'SELECT `id` FROM `base_licenseproduct` WHERE `code`=%s', list1=(k, )).get('id')
        license_certificate_number = query_one(sql=u'SELECT COUNT(*) FROM `base_licenseproductenterprise` WHERE `license_product_id` = %s', list1=(base_licenseproduct_id, )).get('COUNT(*)')
        enterprise_number = len(query(sql=u'SELECT DISTINCT `enterprise_id` FROM `base_licenseproductenterprise` WHERE `license_product_id` = %s', list1=(base_licenseproduct_id, )))
        

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

        data.append((v, enterprise_number, license_certificate_number, patch_2017, inspect_money, inspect_proportion, unit_price, patch_2017_qualified_rate, patch_2016_qualified_rate, ))

    return data


def export_excel(data):
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet(u'许可证', cell_overwrite_ok=True)

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
    file.save(
        '/home/sdu/Project/tools/code/suzhou/statistics_0929/2017监督抽查统计1009.xls')


def main():
    export_excel(handle_data())


if __name__ == '__main__':
    print main()
