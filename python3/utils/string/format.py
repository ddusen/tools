import re
import hashlib


def str_to_md5str(my_str):
    hash_md5 = hashlib.md5(my_str.encode('utf-8'))
    return hash_md5.hexdigest()
    

# 主要用于格式化品牌名称
def format_brand(my_str):
    old_name = my_str
    # 提取中文
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result = pattern.findall(old_name)

    if result:
        if old_name.find('·') != -1:
            new_name = '·'.join([result[0], old_name.split('·')[1]])
        else:
            new_name = ''.join(result)
        return new_name
    return old_name
    
