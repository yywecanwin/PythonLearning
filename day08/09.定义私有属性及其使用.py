# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/30

"""
私有属性
    这样的属性只能在类的里面访问,不能再类的外面访问
定义私有属性的格式:
    self.__属性名 = 属性值

访问私有属性的格式:
    self.私有属性

"""

class Student:

    def __init__(self,name,age,gender):
        self.name = name
        # self.age = age
        # 定义私有属性  __age
        self.__age = age
        self.gender = gender

        pass

    def set_age(self,age):

        if 0 < age <150:
            self.__age = age
        else:
            print("年龄应该在0-150之间,请重新赋值")

    def get_age(self):
        # 返回私有属性的值
        return self.__age

        pass




    def study(self,course):
        print(f"学习{course}")

        pass


    pass


s1 = Student("媳妇",25,"女")
s1.name = "善良的媳妇"

# AttributeError: 'Student' object has no attribute '__age'
# 没有属性 __age,意思是说没有权限访问私有属性
# print(s1.__age)


s1.set_age(100)
# 获得私有属性__age的值
print(s1.get_age())


