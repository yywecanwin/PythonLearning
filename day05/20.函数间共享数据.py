# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

# 定义全局变量

a = 10

def func1():
    #如果在函数外面没有定义变量a,这里就是在定义全局变量
    global a
    a = 10
    #打印全局变量
    print(a)

def func2():
    #打印全局变量
    print(a)

func1()
func2()

