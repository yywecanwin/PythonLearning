# -*- coding: utf-8 -*-
# author：yaoyao time:2020/1/10

# 编写主体框架的代码,在这个文件中掉会用 sms_tools中的函数


"""
学生管理系统——搭建主体框架
"""
from sms import sms_tools

def main():
    """
    主函数
    :return:
    """

    while True:

        # 1、 显示菜单
        sms_tools.show_main()
        # 2、提示录入菜单编号
        menu_code = input("请录入菜单编号：")
        # 3判断菜单编号
        if menu_code == "1":
            # 添加学生
            sms_tools.add_student()

            pass
        elif menu_code == "2":
            # 显示全部学生
            sms_tools.show_all()
            pass

        elif menu_code == "3":
            #查找学生
            sms_tools.find_student()

        elif menu_code == "4":
            # 修改学生信息
            sms_tools.update_student()

        elif menu_code == "5":
            # 删除学生信息
            sms_tools.del_student()

        elif menu_code == "0":
            print("退出系统的功能")
            break;

        else:
            print("录入的菜单编号有误，请重新录入")

if __name__ == '__main__':
    main()















