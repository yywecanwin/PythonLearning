# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
全局变量
    在函数外面定义的变量
特点:
    可以在改程序文件的任何一个地方使用
    前提时先定义后使用
"""

# 定义全局变量
a = 20

def func1(num1,num2):
    print(num1 + num2)
    # 在函数内部对全局变量赋值,并不是修改全局变量的值,而是在定义一个同名的局部变量
    # a = 10
    # print(a) # 10

    #要想在函数内部修改全局变量,必须:
    #1.先声明全局变量:使用关键字global
    global a
    a = 300
    print(a)

func1(12,12)

print(a)




