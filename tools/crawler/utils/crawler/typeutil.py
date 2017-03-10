# -*- coding: utf-8 -*-
from datetime import datetime


def dct_to_obj(obj, dct):
    changed = False
    for k, v in dct.iteritems():
        if hasattr(obj, k) and v:
            if getattr(obj, k) != v:
                setattr(obj, k, v)
                changed = True
    return changed


def merge_dct(dct1, dct2):
    dct = dct1.copy()
    for k, v in dct2.iteritems():
        dct[k] = v
    return dct


def convert(value, t):
    try:
        if t == unicode:
            if isinstance(value, str):
                return unicode(value, 'utf8')
            else:
                return unicode(value)
        elif t == str:
            if isinstance(value, unicode):
                return value.encode('utf8')
            else:
                return str(value)
        elif t == int:
            return int(value) if value else 0
        elif t == long:
            return long(value) if value else 0
        elif t == float:
            return float(value) if value else 0.0
        elif t == datetime:
            if isinstance(value, int) or isinstance(value, long) or isinstance(value, float):
                return datetime.utcfromtimestamp(value)
    except:
        return None

    return None
