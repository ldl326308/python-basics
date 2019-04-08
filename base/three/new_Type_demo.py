# -*- coding:UTF-8 -*-
from base.three.Hello import Hello

h = Hello()
h.say('LiuMing')
# type() 获得对象的类型
print(type(Hello))
print(type(h))


# type() 创建新的类
# 1、需要先定义函数
def info(self, name='Orange'):
    print('Hello, I\'m', name)


# 2、创建Orange class
# 参数1：class的名称
# 参数2：继承的父类集合，如果只有一个父类，注意tuple的单元素写法
# 参数3：class的方法名称与函数绑定，这里是把函数info()绑定到Orange方法名info上
Orange = type('Orange', (object,), dict(info=info))

# 3、使用type()创建的Orange类,调用info()函数
orange = Orange()
orange.info()
orange.info('Yellow Orange')

# type()查看类型
print(type(Orange))
print(type(orange))
