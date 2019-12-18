# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18
"""
1、定义带有参数的函数格式：
    def 函数名(参数1，参数2，参数3)
        函数体

2、给函数设置参数的好处：
    1、扩展的函数的功能，让函数变得的更加通用
    2、让函数的代码变得比较简洁
"""
def sum1(a,b):
    """
        两个数的相加和
    :param a:
    :param b:
    :return: s
    """
    s = a + b
    print(s)
sum1(10,20)
sum1(10,200)
