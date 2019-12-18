# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
局部变量
    在函数中定义的变量,包括形参
特点:
    只能在函数内部使用,不能再函数外面使用

"""
a = 20

def func1(num1,num2):
    print(num1,num2)
    # a就是局部变量
    a = 10
    print(a) # 10

func1(12,12)
# print(num1)

