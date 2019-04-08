# -*- coding:UTF-8 -*-
# OOP：面向对象编程
# 创建一个学生类：Student
# object : 表示Student是从object继承下来的
# 字段以：_字段名 意思是私有的，外部不可对其修改


class Student(object):

    # 初始化
    def __init__(self, name, sex, age):
        self._name = name
        self._sex = sex
        self._age = age

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_sex(self, sex):
        self._sex = sex

    def set_age(self, age):
        self._age = age

    # 打印信息方法
    def print_info(self):
        print('name:%s sex:%s age:%d' % (self._name, self._sex, self._age))

# stu1 = Student('LiuMingkai', '男', 24)
# # Student内部访问是没有问题的
# print(stu1._name)
# stu1.print_info()
