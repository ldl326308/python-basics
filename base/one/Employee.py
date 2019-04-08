# -*- coding:UTF-8 -*-
from types import MethodType


class Employee(object):
    name = 'LiuMingkai'


# 创建一个实例
e = Employee()
# 实例访问类属性 name
print(e.name)
# 类访问类属性 name
print(Employee.name)
# 给实例绑定属性 name
e.name = 'LiuShiyu'
# 实例属性优先级比类属性高，因此，它会屏蔽掉类的属性
print(e.name)
# 类属性并未消失，用Employee.name依然可以访问
print(Employee.name)
# 删除实例属性
del e.name
# 实例的属性name删除后，没有找到就去找类的name属性了
print(e.name)


# 动态绑定方法,由于函数run是要绑定到Employee中
# 所以第一个参数一定是self，未绑定函数的实例是没有的
def run(self):
    print('run........')


emp = Employee()
# 动态绑定函数
emp.run = MethodType(run, emp)
# 调用 run 函数
emp.run()


# 如果你要给所有实例绑定函数，则可以给class绑定函数，所有实例均可用
def say(self):
    print('say .. .. .. ..')


# 给Employee类绑定函数 say
Employee.say = say

emp1 = Employee()
emp1.say()
emp2 = Employee()
emp2.say()

print('_slots_  \r\n')


# Apple类
class Apple(object):
    # _slots_ 限制实例的属性
    __slots__ = ('name', 'color')


# _slots_ : 限制实例能添加的属性
# 对当前类实例起作用，对子类起作用
apple = Apple()
# 给实例添加一个允许实例添加的属性 name
apple.name = '红苹果'


# 给实例添加一个不允许实例添加的属性 age
# apple.age = 90

# 定义一个红苹果类
class RedApple(Apple):
    __slots__ = ('size',)


redApple = RedApple()
redApple.name = 'kkkk'
print(redApple.name)
redApple.color = 'red'
print(redApple.color)
