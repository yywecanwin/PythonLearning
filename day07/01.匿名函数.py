# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/8

"""
def my_add(a,b):
    return a + b

print(my_add(10,20))

"""

# lambda 形参1，形参2，.....:单行表达式 或者 调用其他函数的代数
"""
匿名函数中不能使用 if 语句、while 循环、for 循环, 只能编写单行的表达式，或函数调用, 普通函数都可以.
匿名函数中返回结果不需要使用 return, 表达式的运行结果就是返回结果, 普通函数返回结果必须 return.

"""
my_add = lambda a,b : a + b

sum = my_add(1,2)
print(sum)

