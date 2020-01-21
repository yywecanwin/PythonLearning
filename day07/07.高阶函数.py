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

my_list1 = ['smith', 'edward', 'john', 'obama', 'tom']

def f1(x):
    return x[0].upper() + x[1:]

result1 = map(f1,my_list1)

print(list(result1)) # ['Smith', 'Edward', 'John', 'Obama', 'Tom']

"""
reduce用法
reduce() 函数会对参数序列中元素进行累计.

函数将一个数据集合中的所有数据进行下列操作:
    1、用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作.
    2、得到的结果再与第三个数据用 function 函数运算, 最后得到一个结果.    
"""

"""计算列表中的累加和"""

my_list2 = [1,2,3,4,5]

def f2(x1,x2):

    return x1 + x2

result2 = functools.reduce(f2,my_list2)
print(result2) # 15


"""
filter

filter() 函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象, 如果要转换为列表, 可以使用 list() 来转换.

该接收两个参数, 第一个为函数, 第二个为序列, 序列的每个元素作为参数传递给函数进行判, 然后返回 True 或 False, 最后将返回 True 的元素放到新列表中

"""

"""过滤列表中的偶数"""

my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f3(x):
    return x % 2 == 0

result3 = filter(f3,my_list3)
print(result3)
print(list(result3))
