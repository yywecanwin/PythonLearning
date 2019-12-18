# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
获得函数的返回值的原因
    希望调用函数结束后得到一个结果数据，在后续的代码中使用在这个结果数据

定义带哟返回值的函数的格式
    def 函数名():
        函数体
        return 数据

    这里的return语句使用，返回数据的，这个数据就是返回值
    这个数据 是返回到 函数的调用处

"""

def sum1(a,b):
    """
    两位数相加
    :param a:
    :param b:
    :return: s
    """
    s = a + b
    return s

# 返回值会返回到函数的调用处
# return 30
print(sum1(10,20))





