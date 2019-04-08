# -*- coding:UTF-8 -*-
from extends_demo.Dog import Dog
from extends_demo.Cat import Cat
from extends_demo.Animal import Animal

animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run()
cat.run()

# dir 获得对象的属性和方法
print(dir(dog))

# getattr()、setattr()、hasattr()
# dog 有'x'属性吗
print(hasattr(dog, 'x'))
# 给dog设置属性'x'，值为12
setattr(dog, 'x', 12)
print(hasattr(dog, 'x'))
# 获得dog的属性'x'
print(getattr(dog, 'x'))
# 获取dog属性'num',不存在返回指定值
print(getattr(dog, 'num', 404))
