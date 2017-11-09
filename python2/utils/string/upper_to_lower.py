#!/usr/bin/python
# coding=utf-8
import os

def get_file_path():
    all_path = os.walk(raw_input('请输入待查找的初始目录:'))

    result = []
    for path in all_path:
        for file in path[-1]:
            if file.find(".sql") != -1:
                file = "%s/%s" % (path[0], file,)
                print "Hit:%s %s" % (len(result)+1, file)
                result.append(file)

    return result


def convert_content(file_path):
    operate = raw_input('确认转换吗?[YES/NO]:')
    if operate in ['YES', 'yes', '']:
        for file in file_path:
            content = ""
            with open(file, "r") as r:
                content = r.read().lower()
            with open(file, "w") as w:
                w.write(content)
            print "Excute success: %s" % file

def main():
    convert_content(get_file_path())


if __name__ == '__main__':
    main()
