# -*- coding:UTF-8 -*-

print('循环结合')
# 循环集合，Python中有循环结束执行的函数，如下所示else
# 当然，你不需要也可以去掉
names = ['史森明', '简自豪', '刘世宇']
for name in names:
    print(name)
else:
    print('集合循环结束')

print('数字循环 1 - 10')
# 循环 1 - 10，需要用到一个函数range(起始值，结束值)
# range() 函数可以生成一个整数序列，再通过list()函数转换成list
for i in range(1, 11):
    print(i)
else:
    print('数字循环结束')

print('while循环开始')
# while 循环
n = 0
while n < 10:
    print(n)
    n = n + 1
else:
    print('while循环结束')

print("break、continue的使用")
# 循环中break：结束循环
# continue：跳过此次循环，继续执行下一次
for i in range(1, 20):
    # 当 i 大于10时，用break退出循环
    if i > 10:
        break
    else:
        print(i)

print('使用continue')
# 输出 1 - 10之间的偶数
for n in range(1, 11):
    # n 为奇数是跳过此次循环
    if n % 2 == 1:
        continue
    else:
        print(n)
