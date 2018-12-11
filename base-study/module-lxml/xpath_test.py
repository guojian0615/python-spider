"""
使用lxml模块来进行xpath语法的练习
1、获取所有的tr标签
2、获取第二个tr标签
3、获取所有class等于event的标签
4、获取所有a标签的href属性
5、获取所有职位信息（纯文本）
"""

from lxml import etree

# 打开一个本地文件
html_parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('./data/index.html', html_parser)


# 获取所有的tr标签
def get_all_trs():
    tr_list = html.xpath('//tr')
    for tr in tr_list:
        print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))


# 获取第二个tr标签
def get_second_tr():
    tr_list = html.xpath('//tr[2]')
    print(etree.tostring(tr_list[0], encoding='utf-8').decode('utf-8'))


# 获取所有class等于event的td标签
def get_class_equal_event():
    element_list = html.xpath('//td[@class="event"]')
    for td in element_list:
        print(etree.tostring(td, encoding='utf-8').decode('utf-8'))


# 获取所有a标签的href属性
def get_all_href():
    href_list = html.xpath('//a/@href')
    for href in href_list:
        print(href)


# 获取所有职位信息（纯文本）
def get_all_text():
    position_list = []
    tr_list = html.xpath('//tr[position()>1]')
    for tr in tr_list:
        position = tr.xpath('./td[1]//text()')[0]
        address = tr.xpath('./td[2]/text()')[0]
        number = tr.xpath('./td[3]/text()')[0]
        entry_time = tr.xpath('./td[4]/text()')[0]
        position_info = {
            'position': position,
            'address': address,
            'number': number,
            'entry_time': entry_time
        }
        position_list.append(position_info)
    print(position_list)


if __name__ == '__main__':
    # get_all_trs()
    # get_second_tr()
    # get_class_equal_event()
    # get_all_href()
    get_all_text()
