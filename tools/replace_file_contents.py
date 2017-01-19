#!/usr/bin/python
# coding=utf-8

'''
	4. 编写一个程序, 实现"全部替换"功能, 程序实现如下:

	>>>	dusen@debian:/media/dusen/学习/Python/Learning/029(文件1)$ cat 1.txt
	>>>	好好学习

	>>>	好好学习

	>>>	好好学习

	>>>	好好学习
	...

	>>>	dusen@debian:/media/dusen/学习/Python/Learning/029(文件1)$ python MoveHands_04.py
	>>>	请输入文件名:4.txt
	>>>	未找到该文件或[ [Errno 2] No such file or directory: '4.txt' ]
	>>>	请输入文件名:1.txt
	>>>	请输入你需要替换的单词或字符:习
	>>>	请输入新的单词或字符:编程
	>>>	文件 1.txt 中共有 13 个 [习]
	>>>	您确定要把所有的 [习] 替换为 [编程] 吗?
	>>>	[YES/NO]:yes
	>>>	替换成功^_^



'''


def rw_file(filename):
    file = open(filename, 'r')
    file.seek(0, 0)
    file_content = file.read()
    file.close()

    new_file = replace_str(file_content, filename)

    while new_file == '':

        new_file = replace_str(file_content, filename)

        if new_file != '':
            file = open(filename, 'w')
            file.seek(0, 0)
            file.write(new_file)
            file.close()
            print '替换成功^_^'
            break


def replace_str(file_content, filename):
    old_str = raw_input('请输入你需要替换的单词或字符:')
    new_str = raw_input('请输入新的单词或字符:')

    old_str_count = file_content.count(old_str)

    print '文件 %s 中共有 %s 个 [%s]' % (filename, old_str_count, old_str)

    if old_str_count > 0:
        print '您确定要把所有的 [%s] 替换为 [%s] 吗?' % (old_str, new_str)

        operate = raw_input('[YES/NO]:')

        if operate in ['YES', 'yes']:
            new_file = file_content.replace(old_str, new_str)
            return new_file
        else:
            return ''
    else:
        print '-_-你要替换的字符或单词不存在, 请重试!'
        return ''


def main():
    filename = raw_input('请输入文件名:')
    try:
        rw_file(filename)
    except Exception, e:
        print '未找到该文件或[ %s ]' % e
        main()


if __name__ == '__main__':
    main()
