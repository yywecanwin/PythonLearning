# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/30

class Item:

    def __init__(self,type,area):
        self.type = type
        self.area = area
        pass

    def __str__(self):
        return f"家具类型为{self.type},占地面积为{self.area}"


class House:

    def __init__(self,address,total_area):
        self.address = address
        self.total_area = total_area
        self.free_area = total_area

    # 形参item:家具对象
    def add_item(self,item):
        if self.free_area >= item.area:
            print("添加成功!!!")
            self.free_area -= item.area

        else:
            print("添加失败!!!")

        pass

    def __str__(self):
        return f"房子地址为{self.address},占地面积为 :{self.total_area},剩余面积:{self.free_area}"

    pass

house = House("苏州虎丘区",300)

sofa = Item("鲨鱼皮沙发", 10)
bed = Item("金丝楠木大床", 20)
dt = Item("祖母绿地毯", 300)

house.add_item(sofa)
print(house)

house.add_item(bed)
print(house)

house.add_item(dt)
print(house)







