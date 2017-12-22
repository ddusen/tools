import re
import requests


def get_url():
    r = requests.get(
        'http://www.caict.ac.cn/kxyj/caictgd/201712/t20171214_2229171.htm')
    r.encoding = 'utf-8'

    image_urls = map(
        lambda x: 'http://www.caict.ac.cn/kxyj/caictgd/201712/{0}'.format(x),
        re.findall(r'<p><img style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" oldsrc="(.*?\.jpg)"', r.text)
    )

    return image_urls


def download(urls):
    for i, j in enumerate(urls):
        with open('/home/sdu/Documents/tools/python3/crawler/temp/{0}.jpg'.format(i), 'wb') as img:
            img.write(requests.get(j).content)


def main():
    download(get_url())


if __name__ == '__main__':
    main()
