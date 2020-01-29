# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/29

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        pass

    def study(self,course):
        print(f"学习{course}")

        pass


    """
    是一个魔法方法，比较特殊：
        1.这个方法必须返回一个字符串
        2.python解释器，会在：
            a)打印对象时，自动调用这个方法，得到一个返回值，然后打印返回值
              打印对象打印的是这个方法的返回值
            b）把对象转成字符集传类型的数据时，自动调用这个方法，得到一个返回值 作为 转换后的结果
    
    """


    def __str__(self):

        # return "name:%s,age:%s,gender:%s" % (self.name,self.age,self.gender)
        return f"name:{self.name},age:{self.age},gender:{self.gender}"

        pass

    pass

s1 = Student("hello",20,"男")

# 打印对象默认打印出来的时对象的地址
# 如果在类中定义str方法,打印对象打印出来的时__str__方法的返回值
print(s1) # name:hello,age:20,gender:男

# 类也是一种数据类型,类型的名字就是类名
print(type(s1)) # <class '__main__.Student'>

# 把对象转成 字符串类型:Student -> str
result = str(s1)
print(result)




