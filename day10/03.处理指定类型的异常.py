# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
处理指定类型的异常：
第一种格式：
    try:
        可能出现异常的代码块
    except(异常类1，异常类2，。。。)as 异常对象名：
        处理异常的代码块
"""

print("开始执行。。。。")
try:
    print(10/0)
    f = open("a.txt","r")
    pass
# except(ZeroDivisionError,FileExistsError) as e:
except Exception as e:
    print("处理掉，，，")
    print(e)
print("执行结束")




