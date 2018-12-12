"""
使用正则表达式爬取【古诗文网】推荐诗文信息
"""
import requests
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
}
# 所有的古诗文信息
POETIES = []


def get_detail_info(url):
    """
    获取每页的信息
    :param url:
    :return:
    """
    response = requests.get(url, headers=HEADERS)
    text = response.text
    # re.DOTALL表示.也包含换行符
    # 获取所有的标题
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    # 获取所有的年代
    years = re.findall(r'<div\sclass="cont">.*?<p\sclass="source"><a.*?>(.*?)</a>', text, re.DOTALL)
    # 获取所有的作者
    authors = re.findall(r'<div\sclass="cont">.*?<p\sclass="source"><a.*?<a.*?>(.*?)</a>', text,
                         re.DOTALL)
    # 获取所有的内容
    content_tags = re.findall(r'<div\sclass="cont">.*?<div\sclass="contson.*?">(.*?)</div>', text,
                              re.DOTALL)
    contents = []
    for content_tag in content_tags:
        content = re.sub(r'<.*?>', '', content_tag).strip()
        contents.append(content)

    for poety in zip(titles, years, authors, contents):
        title, year, author, content = poety
        info = {
            'title': title,
            'year': year,
            'author': author,
            'content': content
        }
        POETIES.append(info)


def spider():
    """
    主入口
    :return:
    """
    urls = ['https://www.gushiwen.org/default_1.aspx']
    for url in urls:
        get_detail_info(url)

    print(POETIES)


if __name__ == '__main__':
    spider()
