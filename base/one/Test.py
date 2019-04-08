# -*- coding:UTF-8 -*-
from base.one.Student import Student


# 外部访问Student类
stu1 = Student('LiuMingkai', '男', 24)
# Student内部访问是没有问题的
print(stu1.get_name())
stu1.print_info()
stu1.set_name('LC')
stu1.print_info()