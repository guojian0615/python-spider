"""
1、获取所有的tr标签
2、获取第二个tr标签
3、获取所有class等于event的tr标签
4、获取所有a标签的href属性
5、获取所有职位信息（纯文本）
"""
from bs4 import BeautifulSoup

html_str = """
<table>
    <tbody>
    <tr>
        <td>职位</td>
        <td>地点</td>
        <td>人数</td>
        <td>时间</td>
    </tr>
    <tr class="event">
        <td><a href="/api/index">java开发工程师</a></td>
        <td>合肥</td>
        <td>1</td>
        <td>2018-12-14</td>
    </tr>
    <tr>
        <td>上海</td>
        <td>10</td>
        <td>2018-12-14</td>
    </tr>
    <tr class="event">
        <td><a href="/api/index3">前端开发工程师</a></td>
        <td>合肥</td>
        <td>2</td>
        <td>2018-12-14</td>
    </tr>
    </tbody>
</table>
"""
soup = BeautifulSoup(html_str, 'lxml')
# 获取所有的tr标签
# tr_list = list(soup.find_all('tr'))
# for tr in tr_list:
#     print(tr)

# 获取第二个tr标签
# tr = soup.find_all('tr', limit=2)[1]
# print(tr)

# 获取所有class等于event的tr标签
# tr_list = soup.find_all('tr', attrs={'class': 'event'})
# for tr in tr_list:
#     print(tr)

# 获取所有a标签的href属性
# a_list = soup.find_all('a')
# for a in a_list:
#     print(a['href'])

# 获取所有职位信息(纯文本信息)
tr_list = soup.find_all('tr')
for tr in tr_list:
    print(list(tr.stripped_strings))
