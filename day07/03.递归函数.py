# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/10

"""
递归函数：
    在函数的里面自己调用自己

    定义递归函数的条件：
        1.自己调用自己
        2.必须设置一个终止递归条件

使用递归函数求1-5的累加和
"""


def sum(n):
    # 条件2，设置终止递归的条件
    if n == 1:
        return 1

    else:
        # 条件1：自己调用自己
        return n + sum(n-1)


print(sum(5))



