# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/28

class Student:
    """
    是一个魔法方法
        比较特殊，Python解释器会自动在对象刚刚创建出来之后，立即调用这个方法
        初始化对象：给对象添加属性并赋值
        通过self给对象添加属性：
            self.属性值 = 属性值

            属性是存储在对象里面的
            属性是属于对象的
            访问属性：
                对象名.属性名
    """
    def __init__(self):

        # 添加姓名
        self.name = "姚嵇"
        # 添加年龄
        self.age = 20
        # 添加性别
        self.genderc = "man"
        pass

    def study(self,course):

        print(f"学习{course}")

        pass
    pass


s1 = Student()
s1.study("python")


# 访问属性：对象名.属性名
print(s1.name) # 姚嵇
print(s1.age) # 20
print(s1.genderc) # man

# 修改属性的值
s1.genderc = "female"
print(s1.genderc) # female






