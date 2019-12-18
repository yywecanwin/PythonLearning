# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18
"""
函数：
    具有独立功能的代码块
好处：
    1、让代码结构变得简短，结构更加清晰
    2、提高代码的重复使用率，避免代码重复
    3、把功能的设计和调用进行分离
"""

#打印10次hello world的代码
def print_hello_world():
    i = 1
    while i <= 10 :
        print("hello world")
        i += 1

print("程序已经启动了。。。。。")

# 调用打印10次print_hello_world的功能
print_hello_world()

print("程序运行结束。。。。。")


