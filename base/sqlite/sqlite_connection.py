# -*- coding:UTF-8 -*-
# 内置sqlite驱动，不需要下载
import sqlite3

# 连接SQLite数据库，数据库文件 test.db,如果不存在则当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()

# 删除数据库
cursor.execute('drop table lover')

# 执行创建表的SQL语句
cursor.execute('create table lover (id varchar(5) primary key, name varchar(20) not null)')

# 插入一条数据
cursor.execute('insert into lover(id, name) values (\'E0001\',\'霍建华\')')

# 判断插入是否成功
if cursor.rowcount > 0:
    print('执行成功！')
else:
    print('执行失败！')

# 资源释放
cursor.close()

# 事务提交
conn.commit()

# 关闭连接
conn.close()

# 数据查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询的SQL语句
cursor.execute('select * from lover')

print('-----------数据查询结果---------')
values = cursor.fetchall()
print(values)
