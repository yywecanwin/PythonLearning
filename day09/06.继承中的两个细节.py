# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2


class Father:

    def __init__(self,money,house):
        self.money = money
        self.house = house
        # 私有属性
        self.__girl_friend = "JMJ"
        pass

    def run_company(self):
        print("父亲经营公司。。。")

        pass

    # 私有方法
    def __tia(self):
        print(f"YY与{self.__girl_friend}谈恋爱。。。。")

        pass

    def test(self):
        """
        访问私有属性和方法
        :return:
        """
        print(f"YY与{self.__girl_friend}结婚了")
        self.__tia()

        pass

    pass

# 子类继承父类
class Son(Father):

    def la(self):
        #调用从父亲中继承的test方法
        self.test()
        pass
    pass

s = Son(300000,"6套房子")
s.test()



