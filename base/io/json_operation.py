# -*- coding:UTF-8 -*-

print('\n-------------json格式化-------------')
# json 模块，序列化
import json

d = dict(name='LC', age=20, like='play basketball')
# json.dumps() 序列化
json_str = json.dumps(d)
print(json_str)
# loads() 反序列化
print(json.loads(json_str))

print('-----序列化到文件-----')
# 序列化到TXT文件，以及TXT文件内容反序列化
f = open('E:\\json.txt', 'w')
json.dump(d, f)
f.close()

print('-----文件读取并序列化-----')
f = open('E:\\json.txt', 'r')
json_d = json.load(f)
print(json_d)


print('----------------JSON进阶---------------')


class Student(object):

    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex


