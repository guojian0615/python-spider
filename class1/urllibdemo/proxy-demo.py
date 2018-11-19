"""
代理的使用
"""
from urllib import request

# 不使用代理访问该地址
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print('不使用代理访问的效果：', resp.read())

# 使用代理
proxy_handler1 = request.ProxyHandler({'http': '114.112.70.150:43887'})
opener = request.build_opener(proxy_handler1)
resp = opener.open(url)
print("使用代理后的效果：", resp.read())
