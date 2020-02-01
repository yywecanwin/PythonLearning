# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/1

"""
继承：
    子类继承父类，子类一旦继承父类，就拥有父类中非私有的属性和方法

继承的格式:
    class 子类名（父类名）：
        子类中的代码

继承的好处：
    1.避免了代码重复，提高了代码的重复使用率
    2.扩展了子类的功能

"""

class Father:

    def __init__(self,money,house):
        self.money = money
        self.house = house
        pass

    def run_company(self):
        print("父类经营公司。。。")
        pass
    pass

class Son(Father):
    pass

s = Son(2000000,"前门大街300平米的一套四合院")
print(s.money)
print(s.house)

s.run_company()



