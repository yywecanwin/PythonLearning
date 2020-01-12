# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/11

import functools
my_list = [1,2,3,4,5]

"""
map用法
map()会根据提供的函数对指定序列做映射
第一个参数function以参数序列中的每一个元素用function函数，返回包含每次function函数返回值的新列表
"""

my_list = [1,2,3,4,5]

def f(x):
    return x ** 3

result = map(f,my_list)
print(type(result),result,list(result)) # <class 'map'> <map object at 0x000002246CA0E748> [1, 4, 9, 16, 25]


"""首字母大写"""

my_list = ['smith', 'edward', 'john', 'obama', 'tom']

def f1(x):
    return x[0].upper() + x[1:]

result1 = map(f1,my_list)

print(list(result1))





