# -*- coding:UTF-8 -*-

# metaclass:元类

# 1、模板创建：metaclass是类的模板，必须从type类派生


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 2、指示ListMetaclass来定制类，传入关键字参数metaclass


class MyList(list, metaclass=ListMetaclass):
    pass


# 3、测试
L = MyList()
L.add(1)
L.add(99)
print(L)

