# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/8

def my_funcation(func):
    a = 100
    b = 200
    # 把cucalate_rule当做函数来调用

    result = func(a,b)
    print("result:",result)
my_funcation(lambda a,b:a + b)
my_funcation(lambda a,b:a - b)
my_funcation(lambda a,b:a * b)
