# -*- coding: utf-8 -*-
# author：yaoyao time:2019/9/27
"""
while 循环语句的嵌套
    定义变量，赋值
    while 条件判断语句:
        重复执行代码块
        while 条件判断语句：
            重复执行的代码块
            修改条件语句
        修改条件语句
外面的循环语句，每循环一次，里面的循环语句都会执行完

"""
i  = 1
while i <= 3:
    print("yao is a good man %d" % i)
    j = 1
    while j <= 3:
        print("yao is a nice man %d %d" % (i , j))
        j += 1
    i += 1











