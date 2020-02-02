# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

"""
调用 父类中的被重写的run_company方法，有三种格式：
    1.父类名.方法名(self,参数1，参数2，参数3。。。。)
    2.super(子类名，self).方法名(实参1，实参2，。。。)
    3.super().方法名(实参1，实参2，。。。。)
"""

class Father(): # class Father(object)

    def __init__(self,money,house):
        self.money = money
        self.house = house
        pass

    def run_company(self):
        print("父类经营公司。。。")

    pass

# 子类继承父类
class Son(Father):
    # 重写了父类中的run_company方法

    def run_company(self):
        print("儿子经营公司")
    pass


    def test(self):
        # 调用的是子类中的run_company方法
        # self.run_company()

        # 调用父类中的run_company方法
        # 1.父类名.方法名(self,实参1,实参2，...)
        # Father.run_company(self)
        # 2.super(子类名，self).方法名(实参1，实参2，。。。)
        super(Son,self).run_company()
        #
        pass

pass


s = Son(2000,"江苏省淮安市")
s.test()



