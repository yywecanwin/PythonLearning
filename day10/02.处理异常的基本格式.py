# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/4

"""
基本格式：
    try:
        可能会出现异常的代码块
    except:
        处理异常的代码块

    执行流程：
        如果"可能会出现异常的代码块"出现异常了，就执行”处理异常的代码块“

这个格式可以处理任何一种异常

"""
list1 = [10,20]
print(list1)

try:
    print("数字为%d" % "hello")
    print("hello python")
    pass
except:
    print("变量应该为int类型的")
print("孤独加寂寞，总是，执行不到我。。。")

print("读取一个文件。。。。")




