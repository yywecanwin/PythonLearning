# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
函数的注释：
    对函数进行解释说明的文字
函数的文档注释：
    在函数定义的哪一行的下面添加的多行注释
文档注释的作用
    对函数进行解释说明，提高了函数的可读性


"""

def print_hello_python():
    """
    打印10次hello world
    :return:
    """
    i = 1
    while i <= 10:
        print("hello world")
        i += 1

# 调用函数
print_hello_python()
print()








