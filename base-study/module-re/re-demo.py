"""
python自带模块re正则学习
"""
import re

# search函数会在字符串中查找，而不仅仅从头开始匹配
# text = "this apple is $99 and this mac pro is $4999"
# ret = re.search('.+(\$\d+).*(\$\d+)', text)
# print(ret.groups())

# findall函数查找所有满足要求的字符串
# text = "this apple is $99 and this mac pro is $4999"
# ret = re.findall(r'\$\d+', text)
# print(ret)

# sub用于替换字符串
# text = "this apple is $99 and this mac pro is $4999"
# ret = re.sub('\$\d+', '0', text)
# print(ret)

# compile函数用于预编译正则表达式，可以提高效率
r = re.compile(r"""
    \$ #匹配$符号
    \d+ #匹配至少一个数字
""", re.VERBOSE)
text = "this apple is $99 and this mac pro is $4999"
ret = re.findall(r, text)
print(ret)
