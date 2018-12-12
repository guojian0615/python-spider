"""
使用Beautiful-soup 和requests来爬取【中国天气网】的信息
获取今天全国天气温度最低的前十名城市
使用pyecharts 可视化显示图表信息
"""
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
}
# 保存所有的城市信息
ALL_CITIES = []


def get_city_info(url):
    """
    根据url获取当前页面城市温度信息
    :param url:
    :return:
    """
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('utf-8')
    # 需要特别注意的是，使用lxml解析器针对有些不规范的html会报错
    # soup = BeautifulSoup(text, 'lxml')
    soup = BeautifulSoup(text, 'html5lib')
    div = soup.find('div', attrs={'class': 'conMidtab'})
    # 获取div下所有的table
    tables = div.find_all('table')
    for table in tables:
        # 从每个表格的第二行进行计算,每行就是一个城市信息
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            # 获取每行下所有的单元格
            tds = tr.find_all('td')
            if index == 1:
                city_name = list(tds[1].stripped_strings)[0]
            else:
                city_name = list(tds[0].stripped_strings)[0]
            min_temp = list(tds[-2].stripped_strings)[0]
            ALL_CITIES.append({'city': city_name, 'min_temp': int(min_temp)})


def spider():
    """
    爬虫主入口
    :return:
    """
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        get_city_info(url)
    # 对ALL_CITIES进行排序
    ALL_CITIES.sort(key=lambda data: data['min_temp'])
    data = ALL_CITIES[:10]
    city_names = list(map(lambda city: city['city'], data))
    temps = list(map(lambda city: city['min_temp'], data))
    print(city_names)
    print(temps)

    # 生成本地图表
    bar = Bar("中国天气网最低温度前十城市")
    bar.add("", city_names, temps)
    bar.render()


if __name__ == '__main__':
    spider()
