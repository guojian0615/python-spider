"""
正则表达式，匹配单个字符
re模块是python自带的模块，不需要安装
"""
import re

# 1英文.可以匹配任意一个字符
# text = 'hello'
# result = re.match('.', text)
# print(result.group())

# 2 \s 可以匹配空白字符（\n,\t,\r,空格）
# text = '\n'
# result = re.match('\s', text)
# print(result.group())

# 3 \d可以匹配任意一个数字
# \d 也可以写成 [0-9]
# text = '12334'
# result = re.match('[0-9]', text)
# print(result.group())

# 4 \D 可以匹配非数字的任意一个字符
# \D 也可以写成[^0-9]
# text = '+'
# result = re.match('\D', text)
# print(result.group())

# 5 \w可以匹配a-zA-Z数字，以及下划线_
text = '_afdfdb'
result = re.match('\w', text)
print(result.group())

# \W 可以匹配的内容和\w相反
