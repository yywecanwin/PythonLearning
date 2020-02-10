# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10

a = 100

def func1(a,b):
    return a + b

    pass

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return f"name={self.name},age = {self.age}"

        pass
    pass

# __all__是用来控制 以 from 模块名 import * 这种格式导入的内容的
__all__ = ["a","func1"]


print("module01中的测试代码。。。。")