# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
自定义异常类的原因：
    pYthon解释器自带的异常类不能满足需要

自定义异常类的步骤：
    1.定义一个类，继承一个异常类
    2.在这个类中，添加一个__init__方法；

抛出异常对象的步骤：
    1.创建异常类的对象
    2.使用raise关键字把对象向外抛出



"""
# 1.定义一个类，继承一个异常类
class AgeError(Exception):
    # 2.在这个类中，添加一个__init__方法；
    def __init__(self,msg):
        self.msg = msg


class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.__age = age
        self.gender = gender

        pass

    def set_age(self,age):
        try:
            if 0 <= age < 150:
                self.__age = age
            else:
                # 抛出年龄不合法的年龄
                # 1.创建异常类的对象
                # 2.使用raise关键字把对象向外抛出
                raise AgeError("年龄必须在0-150之间...")
            pass
        except AgeError as ae:
            print(ae)

s = Student("Tom",40,"men")
s.set_age(200)

print("执行结束。。。。")
