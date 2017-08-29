# -*- coding: utf-8 -*-
import re
import time
from mysql import query, query_one, save


def get_html():
    with open("/home/sdu/Project/tools/code/product/product_source.html", "r") as f:
        return f.read()

def main():
    html_source = get_html()
    items = re.findall(re.compile(
        r'_a" class="level(.+?)" treenode_a="" onclick="" target="_blank" style="" title="(.*?)">'), html_source)
    
    for index, item in enumerate(items):
        level = item[0]
        name = item[1]
        if not query(sql=u'SELECT id FROM product WHERE name=%s and level=%s', list1=(name, level, )):
            if level == u'1':
                save(sql=u'INSERT INTO `product`(`name`, `level`) VALUES(%s, %s)', list1=(name, level))
            else:
                parent_id = query(sql=u'SELECT id FROM product WHERE level=%s ORDER BY id DESC LIMIT 0, 1', list1=(int(level)-1, ))[0].get('id')
                save(sql=u'INSERT INTO `product`(`name`, `level`, `parent_id`) VALUES(%s, %s, %s)', list1=(name, level, parent_id))
                
        time.sleep(1)


if __name__ == '__main__':
    main()
