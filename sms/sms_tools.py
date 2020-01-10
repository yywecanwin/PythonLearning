# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/10

# 定义一个列表，用来存储所有学生
student_list = []

def add_student():
    """
    1、添加学生信息
    :return:
    """

    while True:
        # 1、提示录入学生的4个信息
        name = input("请录入姓名：")
        # 判断姓名是否与已有的学生重名
        for student in student_list:
            if name == student.get("name"):
                print("发现重名，请重新录入！！！")
                break

        else:
            # 如果没有重名，就接着录入电话，微信等
            break

    tel = input("请输入电话号码")
    we_chat = input("请录入微信")
    address = input("请录入地址")
    # 2.根据4个信息创建一个字典
    student = {"name":name,"tel":tel,"we_chat":we_chat,"address":address}

    # 3.把字典添加到列表中
    student_list.append(student)
    # 4.提示添加成功
    print(f"添加{name}成功！！！")

    print(student_list)




def show_all():
    """
    2、显示全部学生
    :return:
    """
    # l.判断系统中是否学生信息
    if len(student_list) <= 0:
        # 2.如果没有学生信息，提示系统中还没有xue
        print("系统中还没有学生信息！！！")

    else:
        #3.如果有
        # 3.1打印表头和上面的那条线
        print("姓名".ljust(15) + "电话".ljust(15) + "微信".ljust(15) + "地址".ljust(15))
        print("-" * 60)

        # 3,2遍历学生列表，一个字典打印成一行
        for student in student_list:
            name = student.get("name")
            tel = student.get("tel")
            we_chat = student.get("we_chat")
            address = student.get("address")
            print(name.ljust(15) + tel.ljust(15) + we_chat.ljust(15) + address.ljust(15))
        # 3.3在遍历结束后打印下面的那条线
        print("-" * 50)




# 3、查找一个学生
def find_student():
    # 1。录入一个学生姓名
    input_name = input("请录入一个姓名：")
    # 2.遍历列表
    for student in student_list:
        # 3.判断字典中的姓名与录入姓名是否一样
        if input_name == student.get("name"):
            # 4。如果是一样就打印
            print("姓名".ljust(15) + "电话".ljust(15) + "微信".ljust(15) + "地址".ljust(15))
            print("-" * 50)
            name = student.get("name")
            tel = student.get("tel")
            we_chat = student.get("we_chat")
            address = student.get("address")

            print(name.ljust(15) + tel.ljust(15) + we_chat.ljust(15) + address.ljust(15))
            print("-" * 50)
            break
        else:
            # 5.否则，提示，系统还没有此学生
            print("系统中没有此学生")

# 4、修改一个学生
def update_student():




    pass

# 5、删除一个学生
def del_student():

    pass





def show_main():
    print("*" * 50)
    print("欢迎使用【学生管理系统】v1.0")
    print("1.添加学生")
    print("2.显示学生")
    print("3.查找一个学生")
    print("4.修改一个学生")
    print("5.删除一个学生")
    print()
    print("0.退出系统")
    print("*" * 50)


