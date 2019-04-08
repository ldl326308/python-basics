# -*- coding:UTF-8 -*-
# list 有序集合，是有序、有序、有序的
fruits = ['orange', 'apple', 'banana', 'pineapple']
print(fruits)

# 输出 fruits 集合的长度用函数 len()
print('fruits 集合的长度是：', len(fruits))

# 取出元素语法：集合名称[索引]
# 注意：索引是从 0 开始的，索引可以是负数，如：-1 指的是取集合倒数第一个
print(fruits[0])
print(fruits[-1])

# 添加元素语法：集合名称.append(要添加的内容)
# 这是追加到最后的位置
fruits.append('chestnut')

# 插入到指定位置语法：集合名称.insert(索引, 内容)
fruits.insert(1, 'pear')

# 删除集合元素语法：
# 集合名称.pop()    这是删除最后的
# 集合名称.pop(1)   删除索引是1的元素
fruits.pop()
fruits.pop(1)

# 元素替换语法：集合名称[0] = 'sarah'
fruits[0] = 'sarah'

# list 集合里的元素可以是不同的类型
obj = ['apple', 123, False]

# list 元素也可以是另一个list
obj2 = [obj, '听闻', True]

# 案例2
p = ['java', 'php']
s = ['python', p, 'C#']

# 如果要获得 list 集合 s 中的 Java，可以把这个list看成是一个二维数组
print(s[1][0])

# 第二种有序列表，tuple 和 list 非常相似，tuple 初始化后不可以进行修改
tuple1 = ('java', 'php', 'C#', 'JavaScript')
# tuple 没有append()、insert()这样的方法，获取元素的方式是一样的
print(tuple1[0])
print(tuple1[-1])

# 注意：如果你要定义一个元素的tuple集合，那么在元素的后面要加上","
# "()" 可以表示数学公式中的小括号，也可以表示tuple集合，
# 所以需要在定义一个只有一个元素的tuple时加上"," 来消除歧义
tuple2 = (9,)

# tuple中的元素也可以是一个list
tuple3 = ('a', 'b', ['C', 'D'], 'e')
# 注意：集合tuple3 里的list集合元素是可以改变的，
# 因为list元素改变并没有改变tuple3 指向的 list
tuple3[2][0] = 'X'


