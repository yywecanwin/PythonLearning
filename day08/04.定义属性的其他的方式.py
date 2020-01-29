# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/29

"""
给对象添加属性的3种方式

    1.在__init__方法中，通过self添加属性（推荐的方式）
    2.在其他方式 通过self添加属性
    3.在类的外面，通过对象添加属性

"""

class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

        pass

    def study(self,course):

        #2.在其他方法中 通过self添加属性
        # 第一次执行这行代码时，是给对象添加属性weight，并赋值200
        self.weight = 200

        print(f"学习{course}")

        # 访问属性 stu_num
        print(s1.stu_num)



        pass

    pass


s1 = Student("Tom",18,"男")
print(s1.name)
print(s1.age)
print(s1.gender)

# 调用study方法
# s1.study("Python")
# print(s1.weight)


# 3.在类的外面，通过对象添加属性
s1.stu_num = "20160566146"
print(s1.stu_num)

s1.study("Python")



