# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/4

# 定义父类
class Father:
    def cure(self):
        print("父类给病人治病......")
        pass

    pass

class Son(Father):
    # 重写父类中的方法
    def cure(self):
        print("儿子给病人治病....")

        pass

    pass

"""
鸭子类型
"""

#定义函数，再里面  调用 医生的cure函数
def call_cure(doctor):
    # 调用医生治病的方法
    doctor.cure()
    pass

# 创建父类对象
father = Father()
# 调用函数，把父类对象传递函数
call_cure(father)

# 创建子类对象
son = Son()
# 调用函数，把子类对象传递函数
call_cure(son)






