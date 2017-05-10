#!/usr/bin/python
# coding=utf-8
import os

'''
    功能性描述:
         采用递归查询, 输入文件搜索初始目录, 遇到文件夹自动进入文件夹, 对文件夹中文件进行解析, 实现对文件内容中关键字的替换

    效果如下:
        dusen@ubuntu:/mnt/hgfs/E/Data/Linux-Tools/tools$ python replace_file_contents_v2.0.py
        请输入待查找的初始目录:/home/dusen/Project/crawler/storage/common
        1 > analysis [/home/dusen/Project/crawler/storage/common/.gitlab-ci.yml]
        ....
        文件 /home/dusen/Project/crawler/inspection/common/crawler/service/loader/base.py 中共有 1 个 [__module__]
        您确定要把 [__module__] 替换为 [file_path] 吗?
        [YES/NO]:

                                     ./+o+-
                             yyyyy- -yyyyyy+
                          ://+//////-yyyyyyo
                      .++ .:/++++++/-.+sss/`
                    .:++o:  /++++++++/:--:/-
                   o:+o+:++.`..```.-/oo+++++/
                  .:+o:+o/.          `+sssoo+/
             .++/+:+oo+o:`             /sssooo.
            /+++//+:`oo+o      ok       /::--:.
            \+/+o+++`o++o               ++////.
             .++.o+++oo+:`             /dddhhh.
                  .+.o+oo:.          `oddhhhh+
                   \+.++o+o``-````.:ohdhhhhh+
                    `:o+++ `ohhhhhhhhyo++os:
                      .o:`.syhhhhhhh/.oo++o`
                          /osyyyyyyo++ooo+++/
                              ````` +oo+++o\:
                                     `oo++.
'''


def replace_str(file_content, filename):
    # old_str = raw_input('请输入你需要替换的单词或字符:')
    # new_str = raw_input('请输入新的单词或字符:')

    old_str = '''BaseProductcategory'''
    new_str = '''BaseProduct'''


    old_str_count = file_content.count(old_str)

    if old_str_count > 0:
        print '文件 %s 中共有 %s 个 [%s]' % (filename, old_str_count, old_str)
        print '您确定要把 [%s] 替换为 [%s] 吗?' % (old_str, new_str)

        operate = raw_input('[YES/NO]:')

        if operate in ['YES', 'yes', '']:
            new_file = file_content.replace(old_str, new_str)
            return new_file
        else:
            return ''
    else:
        return ''


def rw_file(filename):
    try:
        file = open(filename, 'r')
        file.seek(0, 0)
        file_content = file.read()

        new_file = replace_str(file_content, filename)

        if new_file != '':
            file = open(filename, 'w')
            file.seek(0, 0)
            file.write(new_file)
            print """
                             ./+o+-
                     yyyyy- -yyyyyy+
                  ://+//////-yyyyyyo
              .++ .:/++++++/-.+sss/`
            .:++o:  /++++++++/:--:/-
           o:+o+:++.`..```.-/oo+++++/
          .:+o:+o/.          `+sssoo+/
     .++/+:+oo+o:`             /sssooo.
    /+++//+:`oo+o      ok       /::--:.
    \+/+o+++`o++o               ++////.
     .++.o+++oo+:`             /dddhhh.
          .+.o+oo:.          `oddhhhh+
           \+.++o+o``-````.:ohdhhhhh+
            `:o+++ `ohhhhhhhhyo++os:
              .o:`.syhhhhhhh/.oo++o`
                  /osyyyyyyo++ooo+++/
                      ````` +oo+++o\:
                             `oo++.
            """

    finally:
        file.close()


def find_file():
    top_path = raw_input('请输入待查找的初始目录:')

    all_ = os.walk(top_path)

    result = []

    count_file = 0
    line = 0
    for each in all_:
        current_top_path = each[0]
        current_folder_list = each[1]
        current_file_list = each[2]

        for current_file in current_file_list:
            count_file += 1

            '''得到当前文件路径'''
            current_file_path = '%s%s%s' % (
                current_top_path, os.sep, current_file)

            print '%s > analysis [%s]' % (count_file, current_file_path)

            '''得到当前文件扩展名'''
            current_file_extension = (os.path.splitext(current_file))[1]

            if current_file_extension in ['.py', '.PY', '.java', '.jsp', '.html']:
                result.append(current_file_path)
    return result


def main():
    result = find_file()
    for filepath in result:
        rw_file(filepath)


if __name__ == '__main__':
    main()
