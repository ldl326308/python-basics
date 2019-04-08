# -*- coding:UTF-8 -*-
# Python内置字典:dict,dict全程dictionary，Java语言中成为map
# 使用键-值(key-value)存储，具有极快的查找速度
scores = {'小明': 95, '小红': 89, '小天': 78}
# 通过 键 去读取 值
print(scores['小明'])
# 通过 键 去写入 值
scores['小红'] = 99

# 使用 in 关键字 判断一个 键 是否存在
print('小明' in scores)

# 通过get()判断 键 是否存在，不存在可以返回自己指定的值
scores.get('小夏', -9)

# 删除使用 pop(key) ，根据 键 删除内容
scores.pop('小明')

# key 是不可变对象


# set和dict类似，是一组key的集合
# 但不存储value，key不能重复
set1 = ([1, 2, 3, 4, 5])
print(set1)

# 重复的元素会自动过滤
set2 = set([1, 1, 1, 23, 4, 3, 2, 4])

# set 添加元素使用 add(key)
# set1.add(6)

# set 删除元素用remove(key),如果没有key值，会抛出异常
# 所以，删除前建议先判断是否存在key
set1.remove(5)

# set 中的 &(交集) 、 |(并集)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 字符串替换 replace('','')
str1 = 'abcde'
print(str1.replace('a', 'A'))
