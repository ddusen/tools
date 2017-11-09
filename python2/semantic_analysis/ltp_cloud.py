#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib

def main():
    text_tuple = ('机动车综合性能检测（有效期以许可证为准）；机动车尾气检测；机动车安全性能检测。(依法须经批准的项目，经相关部门批准后方可开展经营活动)', )
    
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'g1u4Q0o8C0Mz6srJfUEFnJXOEqIZyysZ7NRVYfPp',
        'text': text_tuple[0],
        'pattern': 'dp',
        'format': 'plain'
    }
    
    result = urllib.urlopen(
        url_get_base, 
        urllib.urlencode(args)
        )  # POST method

    content = result.read().strip()

    print content


if __name__ == '__main__':
    main()
