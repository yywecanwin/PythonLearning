# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/4

class Student:

    __kongtiao = "格力空调"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        pass

    """
    定义类方法:
        1.在方法定义的哪一行的上面,使用classmethed装饰器
            这个装饰器的作用
                1.用来表示下面的方法是一个类方法的
                2.在调用类方法是,Python解释器会自动把类名传递cls
        2.第一形参必须是cls,表示类对象,就是那个类名
    
    访问方式:
        1.实例对象,类方法名(实参1,实参2,.....)
        2.类对象.类方法名(实参1,实参2,......)(推荐方法)
    
    特点:
        1.在调用类方法是,python解释器就会自动把类对象传递给cls
        2.只能访问类属性或者类方法,不能访问类实例属性或者实例方法
        
    什么时候定义一个类方法:
        在方法中只需要访问类属性或者类方法,不访问实例属性或者类实例方法
    """

    @classmethod
    def study(cls):
        print(cls.__kongtiao)
        cls.show()
        pass

    @classmethod
    def show(cls):
        print("这个是一个类方法")
        pass

    pass

# 1.实例对象.类方法名(实参1,实参2,....)
s = Student("张柏芝",38,"女")
s.study()

#2. 类对象.类方法(实参1,实参2,.....)
Student.study()
