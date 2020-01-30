# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/30

class SweetPotato:

    def __init__(self):
        self.state = "生的"
        self.total_time = 0

        pass

    def cook(self,time):

        """
        烧烤的方法
        :param time:本次总时间
        """

        # 1.累加烧烤的总时间
        self.total_time += time

        # 2.根据时间修改状态
        if 0 <= self.total_time < 3:
            self.state = "生的"
            pass

        elif 3 <= self.total_time < 6:
            self.state = "半生不熟"
            pass

        elif 6 <= self.total_time < 8:
            self.state = "熟了"
            pass

        elif self.total_time >= 8:
            self.state = "糊了"
            pass

        else:
            print("烤箱坏了....>_<")
            pass

        pass

    def __str__(self):
        if self.total_time > 0:
            return f"总时间:{self.total_time},状态为:{self.state}"
        else:
            return f"总时间:{self.total_time},状态为生的"



    pass

# 创建地瓜对象
sp = SweetPotato()

sp.cook(2)
print(sp)

sp.cook(2)
print(sp)

sp.cook(2)
print(sp)

sp.cook(2)
print(sp)

sp.cook(-10)
print(sp)




