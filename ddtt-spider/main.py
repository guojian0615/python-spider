"""
爬取电影天堂页面最新电影
"""
import requests
from lxml import etree

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
}
BASE_DOMAIN = 'https://www.dytt8.net'


def get_detail_urls_page(page_url):
    """
    获取每页中所有电影详情页面的地址
    :param page_url: 每页的url
    :return: 详情页面地址url列表
    """
    response = requests.get(page_url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    # 获取列表页面html元素
    url_list = html.xpath('//div[@class="co_content8"]/ul')[0]
    detail_urls = url_list.xpath('.//table//a/@href')
    detail_urls = list(map(lambda url: BASE_DOMAIN + url, detail_urls))
    return detail_urls


def get_move_info(url):
    """
    获取每个电影的详细信息
    :param url:
    :return:
    """
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    move = {}
    # 电影图片信息
    images = html.xpath('//div[@id="Zoom"]//img/@src')
    if len(images) > 1:
        move['cover'] = images[0]
        move['snapshot'] = images[1]
    # 电影基本信息
    infos = html.xpath('//div[@id="Zoom"]//p/text()')
    for info in infos:
        if info.startswith('◎片　　名'):
            origin_name = info.replace('◎片　　名', '').strip()
            move['origin_name'] = origin_name
        elif info.startswith('◎译　　名'):
            cn_name = info.replace('◎译　　名', '').strip()
            move['cn_name'] = cn_name
        elif info.startswith('◎上映日期'):
            up_time = info.replace('◎上映日期', '').strip()
            move['up_time'] = up_time
        elif info.startswith('◎片　　长'):
            duration = info.replace('◎片　　长', '').strip()
            move['duration'] = duration
    return move


def spider():
    """
    分页查询所有的最新电影页面,获取每页的详情列表
    :return:
    """
    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for i in range(1, 3):
        detail_urls = get_detail_urls_page(url.format(i))
        for detail_url in detail_urls:
            move_info = get_move_info(detail_url)
            print(move_info)
            movies.append(move_info)


if __name__ == '__main__':
    spider()
