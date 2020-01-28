# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

"""
1.定义类的格式
    class 类名：
        方法列表

2.定义方法的格式
    def 方法名（self,形参2，形参3，。。。）
        方法体

"""

class Student:

    # 吃饭
    def eat(self,food):
        print(f"吃{food}")

    # 睡觉
    def sleep(self,where):
        print(f"睡在{where}")

    # 学习
    def study(self,course):
        print(f"学习{course}")
        print("为了美好的未来加油把")

    pass

# 创建对象的格式：对象名 = 类名（）
s1 = Student()
s1.eat("猪肉")
s1.sleep("房间")
s1.study("书房")


