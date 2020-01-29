# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

class Student:

    """
    在__init__方法中添加了几个形参，用来接收 创建对象时，传递过来的属性值的
    可以在 形参的值，赋值给属性

    """

    def __init__(self,name,age,gender):

        # 添加姓名
        self.name = name
        # 添加年龄
        self.age = age
        # 性别
        self.gender = gender

        pass


    def study(self,course):
        print(f"学习{course}")

        pass

    pass

s1 = Student("姚嵇",20,"男")

# 访问属性：对象名
print(s1.name)
print(s1.age)
print(s1.gender)

s2 = Student("爱你",22,"女")
# 访问属性：对象名.属性名
print(s2.name)
print(s2.age)
print(s2.gender)



