# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

"""
多继承的格式：
    class 子类名(父类1，父类2，.....)
        子类中的代码

"""

class A:

    def __init__(self,a):
        self.a = a
        pass

    def methodA(self):
        print("---------methodA--------")
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
        print("----------methodC---------")
        pass

    def show(self):
        print("show from B")
        pass

    pass


class C(A,B):
    # 为了继承A，B父类中的属性，需要重写init方法，在方法中调用两个父类中的init方法
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)
        pass

    def test(self):
        # 调用A类中的show方法
        A.show(self)
        # 调用B类中的方法
        B.show(self)

        pass
    pass

c = C("a的属性","b的属性")
c.test()
