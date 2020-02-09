# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
finally语句的格式：
    try:
        可能会出现异常的代码块
    except(异常1，异常2，。。。) as 异常对象名：
        处理异常的代码
    finally:
        不管是否出现异常，也不管是否捕获住了，一定执行的代码

    使用场景：
        做释放内存资源的事情
        比如：
            关闭文件
            关闭数据库连接
"""

list1 = [10,20]
try:
    print(list1[3])
except FileExistsError:
    print("索引越界")
finally:
    print("牛逼大了，我一定会被执行")

f = None
f = open("a.txt","r")
try:
    f.write("hello")
    pass
except Exception as e:
    print(e)
    print(10/0)
    pass
finally:
    f.close()
    pass


