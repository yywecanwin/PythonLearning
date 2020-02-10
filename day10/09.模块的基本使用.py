# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
在python言语中，一个,py文件就是一个模块，
    模块文件中可以定义 全局变量，函数，类

    导入模块的原因：
        向在自己的程序文件中，调用另一个程序文件中的 全局变量 函数，类

    导入模块的基本格式：
        import 模块名

    调用格式：
        模块名.全局变量
        模块名.函数(实参1，实参2，...)
        模块名.类(实参1，实参2，。。。)

        这里的 模块名 就是模块文件的名字  但是不包含.py
"""

import module01
import module02

print(module01.a)
print(module01.func1(10,30))
s = module01.Student("Tom",20)
print(s)

print(module02.a)
print(module02.func1(10, 20))




