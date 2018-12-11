"""
正则表达式，匹配多个字符
"""
import re

# 1 *可以匹配0到多个字符
# text = 'hello world'
# result = re.match('\w*', text)
# print(result.group())

# 2 +可以匹配1到多个字符
# text = '123'
# result = re.match('\d+', text)
# print(result.group())

# 3 ?可以匹配0个或者1个
# text = 'hello'
# result = re.match('\d?\w+', text)
# print(result.group())

# 4 {n}可以匹配n个字符
text = '123456'
result = re.match('\d{3}', text)
print(result.group())
