"""
使用lxml模块来解析xml
"""
from lxml import etree

text = """
<div>
    <p id="p1">hello1</p>
    <p id="p2">hello2</p>
</div>
"""


# 使用etree.HTML来解析html字符串
def parse_html():
    html_elment = etree.HTML(text)
    print(etree.tostring(html_elment, encoding='utf-8').decode('utf-8'))


# 使用etree.parse来解析html文件
def parse_file():
    """
    需要注意的是，etree.parse默认的解析器为xml解析器，如果对于html标签不完整的文件
    进行解析，会报错，这时需要传入html解析器
    :return:
    """
    parser = etree.HTMLParser(encoding='utf-8')
    html_elment = etree.parse('./data/index.html', parser=parser)
    print(etree.tostring(html_elment, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    # parse_html()
    parse_file()
