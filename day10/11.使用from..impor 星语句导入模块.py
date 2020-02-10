# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10

"""
导入格式：
    from 模块名 import *
    这里的 * 是通配符，表示 模块文件中所有的内容

访问格式：
    全局变量
    函数（参数1，参数2，。。。）
    类（实参1，实参2，。。。）


"""
import module01
import module02
import sys

# 查看python搜索模块的路径
print(sys.path)

print(module02.a)
print(module01.func1(10, 20))
s = module02.Student("vivi", 25)
print(s)

