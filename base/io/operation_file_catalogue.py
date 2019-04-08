# -*- coding:UTF-8 -*-
import os

# 查看操作系统 nt：Windows    posix：Linux、Unix、Mac OS X
print(os.name)

# 查看环境变量
print(os.environ)

# 获得某个环境变量的值 os.environ.get('key')
print(os.environ.get('JAVA_HOME'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

print('\n---------------------------\n')
# 表示创建目录的完整路径,第一个参数路径，第二个参数新的目录名称
# os.path.join() 就是为了适应在不同的操作系统下也能正确的写出路径
path = os.path.join('E:\\image', 'lyric')
# 创建目录
os.mkdir(path)
# 删除目录
os.rmdir('E:\\image\\lyric')

# 拆分文件路径为：路径 + 文件名
file_path = 'E:\\lyric\\无问.txt'
print(os.path.split(file_path))

# 获得文件的扩展名
print(os.path.splitext(file_path))

# 文件重命名
# os.rename('E:\\file.txt', 'E:\\file_one.txt')

# 删除文件
# os.remove('E:\\file_one.txt')

# 获得当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 获得当前目录下的 .py 文件
for x in os.listdir('.'):
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py':
        print(x)

# 序列化 Python 的 pickle 模块
import pickle

d = dict(name='Lyric', age=21, sex='boy')
# dumps() 序列化成 bytes
print(pickle.dumps(d))

print('\n------------序列化---------------\n')
# dump() 序列化成bytes 并写入文件
d = dict(name='Lyric', age=21, sex='boy')
f = open('E:\\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

print('\n------------反序列化---------------\n')
# 读取bytes并反序列化
f = open('E:\\dump.txt', 'rb')
b = pickle.load(f)
f.close()
print(b)


