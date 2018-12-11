"""
正则小案例
"""
import re

# 手机号码匹配 ，第一位为1，第二位为34578，后面9位为任意数字
# text = '13965011409'
# result = re.match('1[34578]\d{9}', text)
# print(result.group())

# 匹配邮箱 1552869196@qq.com
# text = '155286*9196@qq.com'
# result = re.match('\w+@[a-z0-9]+\.[a-z]+', text)
# print(result.group())

# 匹配url,http/https/ftp://ldfdafd
text = 'http://baidu.com'
result = re.match('(http|https|ftp)://[^\s]+', text)
print(result.group())
