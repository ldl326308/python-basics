# -*- coding:UTF-8 -*-
# 流程控制语句：if、elif、else
age = 20
if age > 30:
    print('age 的值大于 30')
elif age > 18:
    print('age 的值大于 18')
else:
    print("age 的值不大于30也不大于18")

# if 还可以简写，用来判断一个 obj 是非零数值、非空字符串、非空list
x = None
if not x:
    print('x是非零数值或非空字符串或非空list')

# 接收输入内容函数：input()
s = input('birth:')
# 注意：input()返回的数据是string类型
# 需要转换为int才能进行数的比较
birth = int(s)
if birth > 2000:
    print("00后")
else:
    print("00前的老人")





