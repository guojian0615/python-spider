"""
python自带模块json的学习
"""
import json

student_list = [
    {
        'name': 'rose',
        'age': 23,
        'address': 'usa'
    },
    {
        'name': '张山',
        'age': 24,
        'address': '中国'
    }
]

# 将python对象转化为json字符串
json_str = json.dumps(student_list, ensure_ascii=False)
print(type(json_str))
print(json_str)
print('=' * 40)

# 将python对象以json字符串的形式保存到文件中
with open('student.txt', 'w', encoding='utf-8') as fp:
    json.dump(student_list, fp, ensure_ascii=False)

# 将json字符串转化为python对象
json_str = '[{"name": "rose", "age": 23, "address": "usa"}, {"name": "张山", "age": 24, "address": "中国"}]'
students = json.loads(json_str)
print(type(students))
print(student_list)
print('=' * 40)

# 把文件中的内容转化为python对象
with open('student.txt', 'r', encoding='utf-8') as fp:
    students = json.load(fp)
    print(type(students))
    print(students)
