# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/9

"""
如果里面一层函数出现了异常，自己没有处理，那么异常对象就会传递到外面一层函数
如果里面一层函数把异常处理掉了，那么异常对象就不会向外传递了

"""
def func1():
    print("func1开始执行。。。。。")
    # try:
    #     print(10/0)
    #     pass
    # except Exception as e:
    #     print(e)
    print(10 / 0)
    print("func1结束了。。。。")

    pass

def func2():
    print("func2开始执行了。。。。")
    # try:
    #     func1()
    #     pass
    # except Exception as e:
    #     print(e)
    func1()
    print("func2结束了。。。。。")
    pass

try:
    func2()
    pass
except Exception as e:
    print(e)
print("我是后续的代码。。。。")

