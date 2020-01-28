# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28


class Student():

    # 吃饭
    def eat(self,food):
        print(f"吃{food}")

    # 睡觉
    def sleep(self,where):
        print(f"睡在{where}")

        pass

    # 学习
    def study(self,course):
        print(f"学习{course}")

    pass


# 创建对象的格式：对象名 = 类名（）
s1 = Student()
s1.eat("猪肉")
s1.sleep("卧室")
s1.study("书房")

s2 = Student()
s2.eat("牛肉")
s2.sleep("沙发")
s2.study("图书馆")

s3 = Student()
s3.eat("青菜")
s3.sleep("教室")
s3.study("教室")