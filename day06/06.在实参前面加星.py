# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/20

def func1(* a, ** b):
    print("*********8",a) # (10, 20), {'m': 30, 'n': 40})
    print("00000000000",b) # {}

def func2(* args, ** kwargs):
    print("11111111111111",args) # (10, 20)
    print("22222222222",kwargs) # {'m': 30, 'n': 40}

    #调用func1函数
    # func1(args,kwargs)
    # args是一个元组，kwargs是一个字典
    # * 元组：对元组解包，解成，元素1，元素2
    # ** 字典：对字典解包，解成m=30，n=40形成
    func1(* args,** kwargs) # func1(10,20,m=30,n=40)
    # func1()

func2(10,20,m=30,n=40)

















