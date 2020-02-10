# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10


"""
导入格式:
    from 模块名 import 全局变量, 函数, 类
访问格式:
    全局变量
    函数(实参1,实参2, ...)
    类(实参1,实参2, ..)

从 模块名 导入指定内容,内容:全局变量, 函数, 类
"""
# from module01 import a as a01, func1 as f01
# from module02 import a as a02, func1 as f02
from module01 import a, func1
from module02 import a, func1

print(a)
print(func1(10, 20))

print(a)
print(func1(10, 20))


