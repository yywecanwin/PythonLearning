# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/30

class FDJ:

    # 发动机属性
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        pass

    def fire(self):
        print("发动机点火了")
        pass

    pass

class Car:

    def __init__(self,c_brand,c_model,c_fdj):
        self.c_brand = c_brand
        self.c_model = c_model
        self.c_fdj = c_fdj
        pass

    def run(self):

        # 调用发动机，点火的方法
        # 这里的self.c_fdj是一个发动机对象，它里面有fire()方法
        self.c_fdj.fire()
        print("让我带着你一起兜风....")

    pass

# 创建发动机对象
fdj =FDJ("奔驰","model_X6")

car = Car("宝马","x6",fdj)
car.run()

