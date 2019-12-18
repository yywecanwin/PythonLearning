# -*- coding: utf-8 -*-
# author：yaoyao time:2019/12/18

"""
函数的5个细节(重点)
    1.保存函数的返回直
    2.直接打印函数的返回值
    3.函数的返回值作为参数传递给另一个函数
    4.函数中写多个return语句
    5.同一个文件中函数不能重名


"""


def sum(a,b,c):
    return a + b + c

def func1(num):
    print(num)

# 1.使用变量存储函数的返回值
result = sum(12,13,14)
print(result + 1000)  # 1039


# 2.直接打印函数的返回值
print(sum(12,12,12)) # 36

# 3.函数的返回值作为参数传递给另一个函数
# 现指定sum(12,13,14),得到一个返回值,然后把返回值为实参传递func1函数
func1(sum(12,13,14))

# 4函数中写多个return语句
#只执行最上面的return语句,在执行函数时,只要执行了return语句,函数执行到此结束,不再向下执行了
def fun2():
    a = 10
    b = 20

    return a
    return b
    return a + b

print(fun2()) # 10

# return语句后面可以不写返回值,这样表示函数执行到return语句到此结束,函数没有返回值.
def fun3():
    print("hello....")
    return
    print("python...")

fun3()

# 5.同一个文件中函数不能重名
#会使用后面定义的函数覆盖前面同名的函数
def fun4():
    print("没有参数的func4,,,,")

def func4(a, b):
    print(a + b)

func4(12,12)


