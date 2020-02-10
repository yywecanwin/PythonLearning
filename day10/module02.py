# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10

a = 200


def func1(a, b):
    return a - b


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name={self.name}, age={self.age}"


print("module02中的测试代码..")






