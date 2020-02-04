# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/3

"""
类属性
    也是一种属性
    它存储的数据，是所有的实例对象共享共用的数据，在内存中只有一份，不属于某一个实例对象专有，是所有的实例对象共有的

    当某一个数据，是所的实例对象共享共用时，才使用一个类属性，存储这个数据

定义类属性的格式：
    在类的里面，方法的外面定义

类属性的访问方式：
    1.实例对象名.类属性名
    2.类名.类属性名(推荐)

修改类属性：
    类属性只能通过类对象(类名)修改
    不能通过实例对象修改
"""

class Student:
    # 定义类属性
    # 类属性也可以定义成私有，私有的类属性不能在类的外面访问，只能在类的里面访问
    # 定义格式:在类属性前面加两个  下划线
    __kongtiao = "格力空调"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        pass

    def study(self):
        # 1.实例对象名.类属性名
        # print(self.kongtiao)

        # 通过实例对象修改类属性
        # 当通过实例对象修改属性时,并不是真正修改属性,而是定义一个同名实例属性
        # 以后通过实例对象访问这个属性时访问的是实例属性
        self.__kongtiao = "海尔空调"
        print(self.__kongtiao)

        # 2.类名.类属性名(推荐)
        Student.__kongtiao = "美的空调"
        print(Student.__kongtiao)

        print("哈哈哈......")
        pass

    pass


s = Student("冬冬",12,"女")
s.study()
# # 1.实例对象名.类属性名
# print(s.kongtiao)
# # 2.类名.类属性名(推荐)
# print(Student.kongtiao)


