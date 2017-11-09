# -*- coding: utf-8 -*-
import uuid

from mysql import query, query_one, save
from mysql2 import query as query2, query_one as query_one2, save as save2


def handle():
    administrative_penalties_tuple = query(sql=u'SELECT `pubtime`, `publisher`, `case_name`, `illegal_behavior`, `punishment_basis`, `punishment_result`, `penalty_organ`, `credit_code` FROM administrative_penalties')
    for administrative_penalties in administrative_penalties_tuple:
        guid = str(uuid.uuid4())
        cf_wsh = u"—"
        cf_ajmc = administrative_penalties.get('case_name')
        cf_sy = administrative_penalties.get('illegal_behavior')
        cf_zl = u"—"
        cf_yj = administrative_penalties.get('punishment_basis')
        cf_xdr_mc = u"—"
        cf_xdr_shxym = administrative_penalties.get('credit_code')
        cf_xdr_zdm = cf_xdr_shxym[8:-1] if cf_xdr_shxym != u"" else u"—"
        cf_xdr_gsdj = u"—"
        cf_xdr_swdj = u"—"
        cf_xdr_sfz = u"—"
        cf_fr = u"—"
        cf_jg = u"—"
        cf_sxq = None
        cf_jzq = None
        cf_xzjg = administrative_penalties.get('penalty_organ')
        cf_zt = u"—"
        sjc = administrative_penalties.get('pubtime')
        dfbm = u"—"
        bz = u"—"
        cf_bm = u"—"
        cf_syfw = u"—"
        cf_sxyzcd = u"—"
        cf_gsjzq = None
        temp1 = u"—"
        temp2 = u"—"
        temp3 = u"—"
        temp4 = u"—"
        temp5 = u"—"
        gssj = sjc
        prjguid = u"—"
        createtime = sjc
        updatetime = sjc
        p1 = u"—"
        p2 = u"—"
        p3 = u"—"
        if query2(sql=u'SELECT COUNT(*) FROM base_administrativepenalty WHERE cf_ajmc = %s AND cf_sy=%s AND cf_yj=%s AND cf_xzjg=%s AND cf_xdr_shxym=%s AND cf_xdr_zdm=%s', list1=(cf_ajmc, cf_sy, cf_yj, cf_xzjg, cf_xdr_shxym, cf_xdr_zdm, ))[0].get('COUNT(*)') == 0:
            print save2(sql=u'INSERT INTO base_administrativepenalty(`guid`, `cf_wsh`, `cf_ajmc`, `cf_sy`, `cf_zl`, `cf_yj`, `cf_xdr_mc`, `cf_xdr_shxym`, `cf_xdr_zdm`, `cf_xdr_gsdj`, `cf_xdr_swdj`, `cf_xdr_sfz`, `cf_fr`, `cf_jg`, `cf_sxq`, `cf_jzq`, `cf_xzjg`, `cf_zt`, `sjc`, `dfbm`, `bz`, `cf_bm`, `cf_syfw`, `cf_sxyzcd`, `cf_gsjzq`, `temp1`, `temp2`, `temp3`, `temp4`, `temp5`, `gssj`, `prjguid`, `createtime`, `updatetime`, `p1`, `p2`, `p3`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', list1=(guid, cf_wsh, cf_ajmc, cf_sy, cf_zl, cf_yj, cf_xdr_mc, cf_xdr_shxym, cf_xdr_zdm, cf_xdr_gsdj, cf_xdr_swdj, cf_xdr_sfz, cf_fr, cf_jg, cf_sxq, cf_jzq, cf_xzjg, cf_zt, sjc, dfbm, bz, cf_bm, cf_syfw, cf_sxyzcd, cf_gsjzq, temp1, temp2, temp3, temp4, temp5, gssj, prjguid, createtime, updatetime, p1, p2, p3, ))

def main():
    handle()

if __name__ == '__main__':
    main()

