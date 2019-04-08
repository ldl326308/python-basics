# -*- coding:UTF-8 -*-
# @property、@setter、@getter


class Student(object):

    def __int__(self, name, age):
        self._name = name
        self._age = age

    # 可读写
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self, age):
        self._age = age


