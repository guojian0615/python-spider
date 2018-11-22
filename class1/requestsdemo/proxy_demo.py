"""
使用第三方模块requests来完成代理的设置和get请求
"""
import requests
proxy={
    'http':"136.228.128.6:59680"
}
response = requests.get('http://www.httpbin.org/ip',proxies=proxy)
print(response.text)