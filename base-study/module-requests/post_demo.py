"""
使用requests模块来发送post请求
"""
import requests

url_path = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
}
form_data = {'first': 'true',
             'pn': 1,
             'kd': 'python'}
response = requests.post(url_path, data=form_data, headers=heads)
# response.text返回的是解码后的字符串
print(response.text)
