# -*- coding:UTF-8 -*-
import logging
# 设置logging 级别为info
logging.basicConfig(level=logging.INFO)

try:
    print('try开始')
    r = 10 / 1
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
    logging.exception(e)
else:
    print('no error!')
finally:
    print('finally...')
print('end')

print('\r\n ================raise================ \r\n')


# raise：抛出异常
# 自定义异常类
class FooError(ValueError):
    pass


def division(message):
    if len(message) == 0 or message == '':
        raise FooError('value is null or is \'\'')
    else:
        print('print:', message)


# 测试
try:
    division('')
except FooError as e:
    print(e)
finally:
    print('raise end')


# assert 断言,assert 抛出的异常：AssertionError
def foo(name):
    assert len(name) != 0, 'name length is 0'
    print('Hello,', name)


print('-------------------')
foo('听')
print('-------------------')
foo(' ')

# logging:不会抛出异常，可以指定信息级别
logging.info('这是啥')
