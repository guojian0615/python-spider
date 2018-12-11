"""
爬取豆瓣网页正在热映的电影信息
"""
import requests
from lxml import etree

# 构造请求头
header = {
    'Refer': 'https://movie.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
}
url = 'https://movie.douban.com/cinema/nowplaying/hefei/'
response = requests.get(url, headers=header)
text = response.text

# 将text内容解析成html格式的对象
html = etree.HTML(text)
ul_list = html.xpath('//ul[@class="lists"]')[0]
li_list = ul_list.xpath('./li')
move_list = []
for li in li_list:
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    actors = li.xpath('@data-actors')[0]
    image_url = li.xpath('.//img/@src')[0]
    move_info = {
        'title': title,
        'score': score,
        'actors': actors,
        'image_url': image_url
    }
    move_list.append(move_info)

print(f'正在热映的电影信息：{move_list}')
