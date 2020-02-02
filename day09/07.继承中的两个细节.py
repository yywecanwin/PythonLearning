# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/2

class Father:

    def __init__(self,money,house):
        self.money = money
        self.house = house
        pass

    def run_company(self):
        print("父亲经营公司。。。。。")

    pass

class Son(Father):

    # 重写了父类中的init方法
    def __init__(self,name,money,house):
        self.name = name
        # 使用第三种格式调用父类种的__init__方法
        super().__init__(money,house)
        pass

    pass

s = Son("聪聪",200000,"5套别墅")
print(s.name)
print(s.money)
print(s.house)