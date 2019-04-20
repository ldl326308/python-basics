# zip 多个循环同时循环

dic = {i: j for i, j in zip('abcdefg', range(1, 8))}
print(dic)

# enumerate 同时得到位置索引
for index, obj in enumerate('abcdefg'):
    print('{} is {}'.format(index, obj))
