# -*- coding:UTF-8 -*-
from io import StringIO
from io import BytesIO

# StringIO：内存中读写str
f = StringIO()
f.write('hello')
f.write(',')
f.write('LiuMingkai')
# 相当于写入一个文件，读取时也是读取一个文件
# 这里输出：'hello,LiuMingkai'
print(f.getvalue())

print('--------------------')
# 案例2：存入内容是也存入换行，读取时一行一行读取
f = StringIO('Hello!\nI\'m JAVA.\nI like you')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())  # 去掉换行


print('\n--------------------------')
# BytesIO实现在内存中读写bytes
b = BytesIO()
b.write('听闻'.encode('UTF-8'))
print(b.getvalue())

# 读取
by = BytesIO(b'\xe5\x90\xac\xe9\x97\xbb')
print(by.read())
