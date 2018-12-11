"""

"""
from http.cookiejar import MozillaCookieJar
from urllib import request

# MozillaCookieJar 可以将cookie保存到文件中
cookerjar = MozillaCookieJar('data/cookie.txt')
handler = request.HTTPCookieProcessor(cookerjar)
opener = request.build_opener(handler)
opener.open('http://www.baidu.com');
# 保存cookie操作
cookerjar.save()
