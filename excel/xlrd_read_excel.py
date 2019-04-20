# -*- coding:UTF-8 -*-
# Excel的读取操作
import xlrd

# 打开Excel文件
excel_path = 'E:\excel_python.xlsx'
workbook = xlrd.open_workbook(excel_path)

# 获取工作表
# 1、通过sheet页索引
sheet = workbook.sheet_by_index(0)
# 2、通过sheet页数组索引
# sheet = workbook.sheets()[0]
# 3、通过名称
# sheet = workbook.sheet_by_name('听闻')

# 获取行和列数量
rows = sheet.nrows
cols = sheet.ncols

print('行数：', rows, '列数：', cols)

# 获取行列的值,索引 0 开始
row_values = sheet.row_values(0)
print('行内容：', row_values)

cols_values = sheet.col_values(0)
print('列内容：', cols_values)

print('===========循环所有行===========')
# 第一种读取方式
for i in range(rows):
    print(sheet.row_values(i))


print('==============单元格读取=============')
for i in range(rows):
    for j in range(cols):
        print(sheet.cell(i, j).value, end='')

    print()

print('=========行列索引读取方式===========')
# 第二种读取方式，行列索引
for i in range(rows):
    for j in range(cols):
        print(sheet.row(i)[j].value, end='')

    print()

print('=========行列索引读取方式===========')
# 第三种读取方式，行列索引
for i in range(cols):
    for j in range(rows):
        print(sheet.col(i)[j].value, end='')

    print()


