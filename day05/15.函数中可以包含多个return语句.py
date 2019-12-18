# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
一个函数中可以包含多个return语句,但是在执行函数时会根据条件判断的结果,选择其中一个
return语句执行,不能同时执行两个return语句
"""

def get_num(a,b):
    if a > b:
        return a + b
    return a - b

print(get_num(1,2)) # -1
print(get_num(3,1)) # 4



