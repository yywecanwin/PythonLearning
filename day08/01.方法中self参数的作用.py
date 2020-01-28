# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

class Student:

    """
    方法中的self表示  正在调用方法的对象，那个对象正在调用方法，self就表示那个对象
    python解释器能够根据self的值确定是哪个对象正在调用方法
    """

    def study(self,course):
        print(f"学习{course}")
    pass


s1 = Student()
s1.study("python")


s2 = Student()
s2.study("python")


