"""
拉钩网站职位爬虫
"""
from urllib import request
from urllib import parse

url_path = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
}
form_data = {'first': 'false',
             'pn': 2,
             'kd': 'python'}

# 由于发送给服务器的url都需要经过编码操作，所以需要给form_data进行编码
encode_form = parse.urlencode(form_data)

req = request.Request(url_path, data=encode_form.encode('utf-8'), headers=heads, method='POST')

resp = request.urlopen(req)
print(resp.read().decode())
print(resp.geturl())
