# -*- coding:UTF-8 -*-
# 导入MySQL驱动
import mysql.connector

# MySQL 数据库连接
# password设为root口令
conn = mysql.connector.connect(user='root', password='root', database='rpa_employee')
cursor = conn.cursor()

# 创建表
cursor.execute('create table lover (id int primary key auto_increment, name varchar(20) not null)')

# 插入一条记录,mysql占位符%s
cursor.execute('insert into lover(name) values (%s)', ['胡歌'])

# 判断执行是否成功
if cursor.rowcount > 0:
    print('执行成功！')
else:
    print('执行失败！')

# 提交事务
conn.commit()
cursor.close()

# 查询操作
cursor = conn.cursor()
cursor.execute('select * from lover')
values = cursor.fetchall()

# 数据输出
print(values)
