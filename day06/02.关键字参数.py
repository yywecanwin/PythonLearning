# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/19

"""
关键字参数
    在调用函数时，根据形参的名称传递的实参叫做关键字参数

特点
    是根据形参的名称给形参传值得

关键字参数只能卸载实参列表后面

"""

def sum(a,b,c):
    """
    求和
    :param a:
    :param b:
    :param c:
    :return: int
    """

    print(a)
    print(b)
    print(c)
    print(a + b + c)

# 这里的 b=20, a=10, c=30 都是关键字参数
sum(b=20, a=10, c=30)
print("*" * 50)
sum(20,b=20,c=40)
print("*" * 50)
# sum(a=10,b=10)







