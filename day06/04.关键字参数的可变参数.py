# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/19

"""
关键字参数的 可变参数：
    在参数前面加 ** 这个参数叫做，关键字参数的可变参数

"""

def print_arguments(** kwargs):
    print(kwargs) # {'m': 10, 'n': 20}
    print(type(kwargs)) # <class 'dict'>

# 如果以参数的形式， 传递实参，而且 执行的形参名称又不在
# python解释器会自动把，关键参数打包成一个字典，然后把字典传递给带 ** 的可变参数
print_arguments(m=10,n=20)



