# -*- coding:UTF-8 -*-
# xlwt 创建Excel Xls格式文件，以及填入内容
import xlwt


workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('新的sheet页')

chars = 'abcdefghijklmnopqlstuvwxyz哈哈'

n = 0

# 写入26个字符
for i in range(7):
    for j in range(4):
        sheet.write(i, j, chars[n:n + 1].upper())
        print(chars[n:n + 1].upper())
        n = n + 1

# sheet = workbook.add_sheet('新的sheet页', cell_overwrite_ok=True)
workbook.save('E:\\test\\excel_python_write.xls')
