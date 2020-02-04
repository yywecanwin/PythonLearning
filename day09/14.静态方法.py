# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/4

import jingtai


class Student:
    __kongtiao = "格力空调"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        pass

    """
    定义静态方法的步骤:
        1.在方法定义的那一行的上面,使用@staticmethod装饰器
            1.标识下面的方法时静态方法
        2.方法的第一个形参,既不是self也不是cls
    
    特点:
        在方法中不能访问实例属性和实例方法了,因为在它里面得不到self
        通常在这个方法中不访问实例属性和实例方法也不访问属性和类方法
    
    访问方式:
        1.实例对象.类方法名(参数1,参数2,....)
        2.类对象.类方法名(参数1,参数2,.....)(推荐的方式)
    
    在什么时候定义静态方法?
        当在这个方法中既不访问实例属性实例方法,也不访问类属性类方法时
    """

    @staticmethod
    def study():
        print("苏州")
        print("淮安")
        print("徐州")
        pass

    def test(self):
        jingtai.EncodeUtils.encdode("hello","utf-8")
        jingtai.EncodeUtils.decode("hello","utf-8")
        self.study()
        pass

    pass

# 1.实例对象.类方法名(参数1,参数2,......)
s = Student("刘德华",56,"男")
s.study()
s.test()





