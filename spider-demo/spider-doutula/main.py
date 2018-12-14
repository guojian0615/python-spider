"""
[斗图啦]网站图片下周爬虫
"""
import requests
from lxml import etree
import os
import re
from urllib import request


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for image in images:
        image_url = image.get('data-original')
        suffix = os.path.splitext(image_url)[-1]
        file_name = re.sub('[\?？,，\.!！]', '', image.get('alt')) + suffix
        request.urlretrieve(image_url, 'f:\\images\\' + file_name)


def main():
    base_url = 'http://www.doutula.com/photo/list/?page={}'
    for index in range(1, 2):
        url = base_url.format(index)
        parse_page(url)


if __name__ == '__main__':
    main()
