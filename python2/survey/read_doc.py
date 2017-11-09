#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import textract

from docx import opendocx, getdocumenttext

from mysql import query, query_one, save

def get_file_path():
    all_path = os.walk('/mnt/hgfs/Data/work/满意度调查/')

    doc_files = []
    docx_files = []
    for path in all_path:
        for file in path[-1]:
            if file.find(".docx") != -1:
                file = "%s/%s" % (path[0], file,)
                docx_files.append(file)
            elif file.find(".doc") != -1:
                file = "%s/%s" % (path[0], file,)
                doc_files.append(file)

    return (doc_files, docx_files,)


def get_enterprise_name_by_docx(filepath):
    try:
        document = opendocx(filepath)
    except Exception as e:
        return None
    paratextlist = getdocumenttext(document)
    for p in paratextlist:
        if not p.find(u'申报企业'):
            return p.split(u"：")[1].strip()
        else:
            continue

def get_enterprise_name_by_doc(filepath):
    try:
        return textract.process(filepath).split('申报企业名称：')[1].split('\n')[0].strip()
    except Exception as e:
        return None


def insert_data(enterprise_name):
    save(sql=u'INSERT INTO `base_enterprise`(`name`) VALUES(%s)', list1=(enterprise_name, ))


def main():
    doc_list = get_file_path()[0]
    for d in doc_list:
        enterprise_name = get_enterprise_name_by_doc(d)
        if enterprise_name:
            insert_data(enterprise_name)
    
    docx_list = get_file_path()[1]
    for d in docx_list:
        enterprise_name = get_enterprise_name_by_docx(d)
        if enterprise_name:
            insert_data(enterprise_name)


if __name__ == '__main__':
    main()
