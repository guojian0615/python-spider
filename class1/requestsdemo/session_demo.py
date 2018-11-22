"""
使用requests模块的session来操作有连续性的操作
"""
import requests
import json

session = requests.session()
# 登录操作
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3141.7 Safari/537.36',
    "Content-Type": "application/json"
}
login_url = 'http://172.31.205.27:9090/api/v1/authc/login'
login_data = {
    'account': 'jianguo2',
    'password': 'Gj20180214'
}
# 如果请求数据是json的形式，需要借助json.dumps()函数将其转成json形式
login_response = session.post(login_url, json.dumps(login_data), headers=headers)
print(login_response.text)
# 获取项目列表
response = session.get('http://172.31.205.27:9090/api/v1/project/listProject')
print(response.text)
