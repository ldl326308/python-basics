# -*- coding:UTF-8 -*-

# 文件读取
try:
    f = open('E:\python_io_operation.txt', 'r', encoding='UTF-8')
    content = f.read()
    print(content)
except IOError as e:
    print(e)
finally:
    # 资源释放
    if f:
        f.close()
    print('file read end')

# with 语句，自动帮我们关闭close()
with open('E:\python_io_operation.txt', 'r', encoding='UTF-8') as f:
    print(f.read())

# 一行一行读取
f = open('E:\python_io_operation.txt', 'r', encoding='UTF-8')

# readlines 返回一个list
for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'去掉

print('--------字节读取--------')
f = open('E:\python_io_operation.txt', 'r', encoding='UTF-8')
# 按字节读取内容
print(f.read(10))

print('------------二进制文件读取，图片、视频...---------------\r\n')
# 二进制文件读取，图片、视频、音频....
f = open('F:\LiuDilin\MyImg\software-img\wallpaper.png', 'rb')
print(f.read())
f.close()  # 资源释放

print('\r\n-------------文件写入----------------\r\n')
# w：写文本  wb:写二进制  encoding:写入编码格式
# 注意：如果文件不存在，会帮你创建文件，再写入内容，如果存在，会覆盖
# 第二个参数：
# r：开放阅读(默认)
# w：打开写入，现截断文件
# x：打开以进行独占创建，如果文件已存在则失败
# a：打开以进行写入，如果存在则附加到文件的末尾
# b：二进制模式
# t：文字模式(默认)
# +：打开磁盘文件进行更新(读写)
f = open('E:\python_write.txt', 'w', encoding='UTF-8')
f.write('你站在桥上看风景，我在桥下看你。')
f.close()  # 资源释放

