"""
正则表达式，案例学习
"""
import re

# 1 脱字符^有两种含义，一个表示以什么开头，一个在[]中表示排除该元素
# text = 'hello world'
# ret = re.search('^o', text)
# print(ret.group())

# 2 $表示以什么结尾
text = 'hello rose'
ret = re.search('.*rose$', text)
print(ret.group())
