# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/1

"""
子类不能继承父类中私有的属性和方法
"""

class Father:

    def __init__(self,money,house):
        self.money = money
        self.house = house
        # 私有属性
        self.__girl_friend = "JiMJ"
        pass

    def run_company(self):
        print("我们结婚了。。。")

        pass


    # 私有方法
    def __tia(self):
        print(f"YY与{self.__girl_friend}谈恋爱。。。")
        pass




# 子类继承父亲
class Son(Father):

    def test(self):
        # print(self.__girl_friend)
        self.__tia()
        pass

    pass

s = Son(200000,"江苏省淮安市")
print(s.money)
print(s.house)
s.run_company()

# print(s.__girl_friend)

s.test()



