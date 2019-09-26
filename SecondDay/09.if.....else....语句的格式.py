# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
2.if...else...语句格式

    if 关系表达式:
        语句体1
    else:
        语句体2

    执行流程:
        1.先执行 关系表达式, 看其结果是True还是False;
        2.如果是True,就执行 语句体1;
        3.否则就执行语句体2;
"""
str_age = input("请录入一个年龄:")
age = int(str_age)

if age >= 18:
    print("已经成年!!!")
    print("欢迎进入网吧下载小电影看哦!!!!")
else:
    print("小朋友,你还是回家写作业吧....")

print("我是if语句格式之外的代码,一定会被执行...")