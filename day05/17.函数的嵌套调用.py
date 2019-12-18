# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

def func1(a,b):
    s = a + b
    print(f"func1中的s:{s}")

def func2():
    print("开始调用func2......")
    func1(12,12)
    print("func2结束了.....")
func2()