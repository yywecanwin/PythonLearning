# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10

# 定义 学生类

class Student:

    def __init__(self,id,name,score):
        self.id = id
        self.name = name
        self.score = score

        pass

    def __str__(self):
        return f"{self.id},{self.name},{self.score}"