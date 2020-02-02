# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

"""
重写父类中的方法的原因：
    父类中的方法不能满足子类的需要，但是子类又想保留这个方法名
重写父类中的方法
    这就需要子类中定义一个同名的方法，这叫重写父类中的方法

如何重写：
    1.把父类中的方法复制粘贴到子类中
    2.在子类中秀修改方法体

特点：
    子类重写了父类的方法后，当通过子类对象调用这个方法时，调用的是子类中的这个方法

"""

class Father: # class Father(object)

    def __init__(self,money,house):

        self.money = money
        self.house = house

        pass

    def run_company(self):
        print("父亲经营公司。。。。。")

        pass


    pass


# 子类继承父类
class Son(Father):

    def run_company(self):
        print("儿子经营公司。。。。")
        pass
    pass

s = Son(200000,"江苏省淮安市")
print(s.house)
print(s.money)
s.run_company()

