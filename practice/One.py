# -*- coding:UTF-8 -*-


# 1、2、3、4 组成不同、不重复的三位数
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)

# 输入三个数，按大小输出
# L = []
# for i in range(3):
#     number = int(input('请输入：'))
#     L.append(number)
#
# L.sort()
# print(L)

# 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0} * {1} = {2}  '.format(i, j, i * j), end='')

    print('')
