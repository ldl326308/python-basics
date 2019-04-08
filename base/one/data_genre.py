# -*- coding:UTF-8 -*-

# 1、数据类型
number1 = 10
number2 = 10.2
str1 = '这是一个字符串'
# 注意布尔值的关键字首字母要大写
flag = False
obj = None

print('输出函数print()的相关用法')
# 输出函数 print()
print(number1)
print('哈哈', str1)
print('''
    这
    个
    就
    牛
    掰
    了
''')

print('转义符的使用=========')
# 转义符
print('我是\'刘地林\'')

# 加字母 r 在输出语句最前面，输出内容不再被转义
print(r'我是\\\n\\')
print('\n')

print('逻辑运算符 and or ')
# 逻辑运算符 and or
print(True and True)
print(False or True)
print(6 > 9 and 4 > 7)
print(3 > 4 or 6 > 2)

print('单目运算符 not ')
# 单目运算符 not
print(not True)
print(not 1 > 2)

print('两种除法 "/" 和 "//" ')
# 两种除法：第一种 '/' 第二种 '//'
print(10 / 3)
print(9 / 3)
print(10 // 3)

print("运算符 % ")
print(20 % 9)



