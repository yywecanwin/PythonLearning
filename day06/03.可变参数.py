# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/19

"""
可变参数
    在形参前面加了一个 *，这个参数就叫可变参数（不定长参数）
    表示0 个或者无数个形参

特点：
    1、前面有一个 *
    2、表示0和或者任意多个形参

好处：
    1、可以扩展函数得功能，更加通用


"""

def print_arguments0():
    print()


def print_arguments1(a):
    print(a)

def print_arguments2(a,b):
    print(a)
    print(b)

def print_argumemts3(a,b,c):
    print(a)
    print(b)
    print(c)

def print_arguments(* args):
    # print(* args) # 解包：10 20
    # print(args) #(10, 20)
    # print(type(args)) # <class 'tuple'>
    # 遍历args
    for e in args:
        print(e)





# 如果函数的形参是一个可变参数，当调用函数时，python解释器会自动吧传递的
# 实参打包成一个元组，然后把元组传递给可变参数
print_arguments(10,20)
print_arguments(10,20,30)





