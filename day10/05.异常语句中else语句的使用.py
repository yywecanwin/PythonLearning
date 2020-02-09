# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
else 语句的格式：
    try:
        可能会出现异常的代码块
    except(异常类1，异常2，。。。。) as 异常对象名：
        处理异常的代码块
    使用场景:
        通常用来检测是否出现异常了

"""
list1 = [10,20]
try:
    print(list1[1])
    print(list1[2])
    pass
except:
    print("索引越界")
    pass
else:
    print("没有异常，说明索引没有越界")


