# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

"""
多层继承
    一层一层的继承
就是单继承

"""

class A:

    def __init__(self,a):
        self.a = a
        pass

    def methodA(self):
        print("---------methodA---------")

    pass

class B(A):

    def __init__(self,a,b):
        self.b = b
        super().__init__(a)
        pass

    def methodB(self):
        print("---------methodB--------")
        pass
    pass

class C(B):
    def __init__(self,a,b,c):
        self.c = c
        # 调用父类__init__方法
        super().__init__(a,b)
        pass

    def methodC(self):
        print("--------methodC-------")
        pass

    pass



obj_c = C("a的属性","b的属性","c的属性")

print(obj_c.a)
print(obj_c.b)
print(obj_c.c)

obj_c.methodC()
obj_c.methodB()
obj_c.methodA()

#
