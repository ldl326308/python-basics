# -*- coding:UTF-8 -*-
# 函数，定义函数关键字 def
# 定义一个求和的函数 sum

def summation(number_one, number_two):
    return number_one + number_two


number1, number2 = 20, 10

# 函数调用
number3 = summation(number1, number2)
print(number3)


# 默认参数：如果第二个参数不输入，默认第二个参数为18
# 注意：默认参数指向不变对象
def hello(name, age=18):
    print('我叫', name, '今年', age, '岁')


# 函数调用
hello('LiuDilin', 20)
hello('LiuMingkai')

print('参数为可变对象，及其发生的问题')


# 参数为可变对象，及其发生的问题
def add_end(L=[]):
    L.append('end')
    return L


# 调用 add_end()
# 第一次执行函数，L = [] ,返回的集合最后被追加了一个'end'元素
print(add_end())
# 第二次执行函数，L 指向的不在是一个空的 集合
print(add_end())

print('参数为不可变对象')


def add_end_two(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 调用 add_end_two()
print(add_end_two())
print(add_end_two())
print(add_end_two())

print('=============关键字参数===========')


# 关键字参数
def person(name, age, **lc):
    print('name:', name, 'age:', age, 'other:', lc)


# 调用
person('Michael', 30)
person('Bob', 20, city='珠海', money=88.0)

extra = {'city': '珠海', 'money': 88.0}
person('LiuDilin', 20, **extra)


def say(name, age, *kw):
    print('name:', name, 'age:', age, kw)


say('LiuDilin', 20, 'a', 'b', 'c')


def hello(name, age, *args, city, money):
    print(name, age, args, city, money)


arr = (2, 3, 6, 7)
hello('LiuMingkai', 20, arr[0], arr[1], city='Guangzhou', money=20.9)


def hear(name, *args, **age):
    print(name, age)
