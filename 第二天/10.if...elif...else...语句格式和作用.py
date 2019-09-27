# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27

"""
3.第三种格式
    if 关系表达式1：
        语句体1
    elif 关系表达式2：
        语句体2
    ....
    else：
        语句体n+1

    执行流程：
        1.先执行  关系表达式1，看其结果True还是False
        2.如果是True，就执行  语句体1，后面的就不再执行了
        3.如果False，就执行 关系表达式2，看起结果是True还是False
        4.如果是True就执行 语句体2，后面的就不再执行了
        5，如果False，就执行  下一个  关系表达式 ，看其结果是True还是False
        6.如果以上所有的表达式的结果都是False，就执行else下面的  语句体n+1

    else 语句可以写，也可以不写，根据实际需要决定

"""
week = int(input("请录入一个1-7之间的数字："))

if week == 1:
    print("yao is a good man")
elif week == 2:
    print("yao is a handsome man")
elif week == 3:
    print("yao is a nice man")
elif week == 4:
    print("yao is a rightful man")
else:
    print("......................")


