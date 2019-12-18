# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
1、函数的定义格式
    def 函数名():
        函数体
    这里的 函数体 就是一个代码块，可以是一行或者多行代码

    如果只定义函数，没有调用函数，函数里面的代码 是不会被执行的

2、函数的调用格式：
    函数名（）
"""

def sum1():
    s = 4 + 5
    print(s)

def print_hello_sum1():
    i = 1
    while i <= 10:
        print("hello world")
        i += 1

#调用sum1函数
sum1()

# 调用print_hello_sum1函数
print_hello_sum1()

