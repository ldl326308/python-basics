# -*- coding:UTF-8 -*-
# import iteration as iteration
from collections import Iterable
from functools import reduce
import functools

print('Python高级编程')
# 高级编程
print('list 切片')
names = ['简自豪', '刘明凯', '史森明', '刘世宇', 'LiuDilin']
# 取出前三个元素 0-3 ，不包括索引3，也就是0,1,2
print(names[0:3])
print(names[1:3])
print(names[-3:-1])

# 初始化一个list集合，元素是0-99
L = list(range(0, 100))
# 取前十个
print(L[0:10])
# 取最后十个
print(L[-10:])
# 取前十个数，每两个取一个
print(L[0:10:4])
# 所有数每个5个取一个
print(L[0::5])
# 复制一个 list
M = []
M = L[:]
print(M)

print('tuple切片')
# tuple 切片
T = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 取前三个元素
print(T[:3])
print(T[-3:])

print('字符串切片')
# 字符串切片
print('ABCDEFGHIJK'[0:3])
print('ABCDEFGHIJK'[0::2])

# dict 迭代
d = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# 迭代所有key值(默认迭代key值)
for key in d:
    print(key)
else:
    print('迭代key值结束\r\n')

# 迭代所有value值
for value in d.values():
    print(value)
else:
    print('迭代所有value值结束\r\n')

# key 和 value 一起迭代
for k, v in d.items():
    print('key:', k, 'value:', v)
else:
    print('key和value一起迭代结束')

# 判断一个object是否可以迭代
# print(isinstance('abc', iteration))
# print(isinstance([1,2,3], iteration))
# print(isinstance(123, iteration))

# 如果循环list你需要同时循环索引和值，使用enumerate函数
arr = ['L', 'O', 'V', 'E']
for i, value in enumerate(arr):
    print(i, value)
else:
    print('循环结束了')

# 扩展，另一种循环奇怪数据结构的方式
for x, y in [(1, 'A'), (2, 'B'), (3, 'C')]:
    print(x, y)
else:
    print('奇奇怪怪的循环结束了')

print('生成一个集合[1*1,2*2,3*3....,10*10]')
# 比如要生成一个集合[1*1,2*2,3*3....,10*10]
# 第一种方式，通过循环得到
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 第二种方式，进阶
X = []
X = [x * x for x in range(1, 11)]
print(X)

# 在上面的基础上得到只要偶数的乘积
Z = []
Z = [x * x for x in range(1, 11) if x % 2 == 0]
print(Z)

# 循环两个字符串，两个字符串循环的字符拼接，组成新的字符串
print([m + n for m in 'ADC' for n in 'XYZ'])

# dict 类型用循环键值对拼成字符串，保存在list
d = {'史森明': '98', '刘世宇': '95', '刘明凯': '95'}
print([k + '=' + v for k, v in d.items()])

# 把list集合中所有的字符变成小写
L = ['Hello', 'Why', 'IBM', 'Orange']
print([s.lower() for s in L])
print([s.upper() for s in L])

# 判断一个变量是不是字符串
x = 'abcdefg'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

print('生成器:generator')
# 生成器:generator
g = (x * x for x in range(10))
print(g)
# 生成器数据打印
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 通过for循环迭代
print('for循环迭代')
for z in g:
    print(z)

# while next() 迭代 generator
# while True:
#     try
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# isinstance 判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abcdefg', Iterable))


# 高阶函数：函数可以作为参数，传入另一个函数中使用
def deep_love(a, b, fun):
    return fun(a) + fun(b)


print(deep_love(-10, 20, abs))


# map、reduce
def f(x):
    return x * x


# map(函数,数据)，返回一个Iterator，是惰性序列，
# 通过list()函数把整个序列计算出来返回一个list
m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(m))

# 用map把一个数字集合转成字符串
print(list(map(str, [23, 44, 5, 66, 78, 98])))


# reduce，把一个函数作用在一个序列上，这个函数必须接收两个参数
# 求和的计算
def add(x, y):
    return x + y


# 一个集合的求和计算
print(reduce(add, [1, 3, 5, 7, 9]))
print(sum([1, 3, 5, 7, 9]))


# 案例2 把集合[1,3,5,7,9] 变成 13579
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 案例3 字符串集合转数字
def char_to_num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char_to_num, '13579')))


# 练习用map()函数，把输入的字母组成的字符串开头字母大写，其余小写
def normalize(name):
    return name[0].upper() + ''.join(list(map(lambda x: x.lower(), name[1:])))


print(normalize('fsKKKKLSF'))

print('==============filter()函数==============')


# filter() 函数，用于过滤序列,参数接收一个函数及一个序列
# 定义一个函数，被3整除返回 True，否则返回 False
def is_divisibility3(number):
    return number % 3 == 0


# 保留被3整除的数
print(list(filter(is_divisibility3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])))


# 删除一个集合里的空字符串
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, [' ', 'a', 'b', 'e', '', 'F'])))

print('sorted排序算法，小到大')
# sorted 排序算法
print(sorted([36, 3, -10, 92, 1, -40]))
# 按绝对值来排序
print(sorted([36, 3, -10, 92, 1, -40], key=abs))

# 字母字符串排序
# 开始字母ASCII的大小比较，大写字母Z会排在小写a前面
print(sorted(['Abc', 'Money', 'abc', 'Orange', 'banana']))
# 忽略大小写，则可以传入一个字母转大写或小写的函数
print(sorted(['Abc', 'Money', 'abc', 'Orange', 'banana'], key=str.lower))
print(sorted(['Abc', 'Money', 'abc', 'Orange', 'banana'], key=str.upper))
# 如果需要反向排序，传入第三个参数 reverse=True
print(sorted(['Abc', 'Money', 'abc', 'Orange', 'banana'], key=str.upper, reverse=True))

print('匿名函数')
# 匿名函数：lambda 参数:表达式(返回Boolean值)
# 取偶数
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print('===========装饰器Decorator=============')


# 装饰器：Decorator
# 自我介绍的函数

# 加上装饰器，在调用self_introduction函数前输出'开始自我介绍'
def prefix_message(func):
    def wrapper(*args, **kw):
        print('开始自我介绍')
        return func(*args, **kw)

    return wrapper


@prefix_message
def self_introduction(name, age, likeMsg):
    print('我叫', name, '今年', age, '岁', '我喜欢', likeMsg)


self_introduction('LiuDilin', 20, '打篮球')

print('偏函数\r\n')
# 偏函数
print(int('211122'))
# base：进制
print(int('211122', base=8))
# 转2进制
print(int('70226', base=2))

# functools.partial 创建偏函数
int2 = functools.partial(int, base=2)
print(int2('000000001111111111'))
