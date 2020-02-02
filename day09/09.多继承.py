# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

"""
多继承的格式：
    # 优先继承父类1
    class 子类名(父类1，父类2，。。。。)
        子类中的代码
"""

class A:
    def __init__(self,a):
        self.a = a
        pass

    def methodA(self):
        print("--------methodA--------")
        pass

    def show(self):
        print("show from A")
        pass

    pass

class B:
    def __init__(self,b):
        self.b = b
        pass

    def methodB(self):
        print("--------methodB---------")
        pass

    def show(self):
        print("show from B")
        pass

    pass

# 让C类同时继承A，B两个父类
class C(A,B):
    # 为了继承A,B两个父类中的属性，需要重写init方法，在方法中调用两个父类中的init方法

    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)
        pass
    pass

c = C("a的属性值","b的属性值")
print(c.a)
print(c.b)

c.methodA()
c.methodB()
c.show()

