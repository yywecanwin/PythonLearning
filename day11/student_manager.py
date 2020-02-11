# -*- coding: utf-8 -*-
# author：yaoyao time:2020/2/10

# 对 学生 管理系统的 主要功能

from student import *

class StudentManager:

    def __init__(self):
        # 添加一个字典，用来存储所有的学生
        # 学号作为key，学生对象 作为 value
        self.student_dict = {}
        pass

    def start(self):
        """
        启动学生管理系统

        """
        # 5.把以上4个步骤循环起来
        while True:

            # 1.显示菜单
            # print("调用 显示菜单 的功能")
            self.show_menu()


            # 2.提示录入菜单编号
            menu_code = input("请录入菜单编号")

            # 3.判断菜单编号
            # 4.根据判断的结果调用对应的功能
            if menu_code == "1":
                print("调用1.添加的学生的功能")
                self.add_student()
                pass
            elif menu_code == "2":
                # print("调用2.显示全部 的功能")
                self.show_all()
                pass
            elif menu_code == "3":
                # print("调用3.查询学生 的功能")
                self.find_student()
                pass
            elif menu_code == "4":
                # print("调用1.修改学生 的功能")
                self.update_student()
                pass
            elif menu_code == "5":
                # print("调用1.删除学生 的功能")
                self.delete_student()
                pass
            elif menu_code == "0":
                print("调用1.退出系统 的功能")
                break
                pass
            else:
                print("录入的菜单编号有误，请重新录入")
        pass

    def show_menu(self):
        """
        显示菜单
        """
        print("*" * 40)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.显示全部")
        print("3.查询学生")
        print("4.修改学生")
        print("5.删除学生")
        print()
        print("0.退出系统")
        print("*" * 40)

        pass


    def add_student(self):
        # 1.提示录入一个学号

        # 这段代码,控制不能录入重复的学号的
        while True:
            id = input("请录入一个学号:")

            # 2.判断学号是否重复，如果重复，需要重新录入
            if id in self.student_dict:
                continue
                pass
            else:
                break
        # 3.提示录入姓名和分数
        name = input("请录入一个姓名")
        score = input("请录入一个分数")

        # 4.使用录入新的学号，姓名，分数创建一个学生对象
        s = Student(id,name,score)

        # 5.把学号作为key,对象作为value,添加到字典
        self.student_dict[id] = s
        # 6.提示添加成功
        print(f"添加{id}成功")

        pass

    def show_all(self):
        """
        显示全部学生
        """

        # 先判断系统中是否有学生信息,如果有
        if len(self.student_dict) > 0:

            # 1.打印表头,和上面的那条线
            print("学号".ljust(15) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            # 2.得到字典中所有的value组成的列表
            student_list = self.student_dict.values()
            # 3.遍历列表,每一元素都是一个学生对象
            for student in student_list:
                # 4.在循环里,得到学号,姓名,分数,打印成一行
                id = student.id
                name = student.name
                score = student.score
                print(id.ljust(15) + name.ljust(15) + score.ljust(15))
                pass


            # 5.在循环结束后,打印下面那条线
            print("-" * 45)
            pass

        else:
            # 如果系统中没有学生信息,就提示"系统中还没与学生信息"
            print("系统中还没有学生信息")

            pass
        pass

    def find_student(self):
        """
        根据学号查询一个学生
        :return:
        """

        # 1.提示录入学号
        id = input("请输入一个学号")

        # 2.查找学号在系统是否存在
        if id not in self.student_dict:

            # 3.如果不存在,就是提示系统中没有次学生
            print("系统中的没有此学生!!!!!")
            pass
        else:
            # 4.如果存在
            # 4.1打印 表头和那条线
            print("学号".ljust(15) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            # 4.2得到这个学号对应的学生对象
            s = self.student_dict.get(id)
            # 4.3得到 学号,姓名,分数,打印成一行
            id = s.id
            name = s.name
            score = s.score
            print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            # 4.4 打印出下面的那条线

            print("-" * 45)
            pass


        pass

    def update_student(self):
        """
        根据学号修改一个学生
        """
        # 1.提示录入学号
        id = input("请录入一个学号")
        # 2.查找学号在系统是否存在
        if id not in self.student_dict:
            # 3.如果不存在,就提示系统中没有此学生
            print("系统中没有此学生!!!!")
            pass
        else:
            # 4.如果有,提示请录入新的姓名和分数
            name = input("请录入新的姓名")
            score = input("请录入新的分数")
            # 5.根据学号从字典中得到 学生对象
            s = self.student_dict.get(id)
            # 6.使用新录入的姓名和分数,修改学生对象中的姓名和分数
            s.name = name
            s.score = score

            # 7.提示成功
            print(f"修改{id}成功")

            pass





        pass


    def delete_student(self):
        """
        根据学号删除一个学生
        """

        # 1.提示录入学号
        id = input("请录入一个学号")
        # 2.查找学号在系统是否存在
        if id not in self.student_dict:
            # 3.如果不存在,就提示系统中没有此学生
            print("此系统中没有此学生")


            pass
        else:
            # 4.如果有,从字典中把该学号对应的键值对删除
            self.student_dict.pop(id)
            pass

        # 5.提示删除成功
        print(f"删除{id}成功")


        pass


    def dict_to_file(self):
        """
        把字典的学生的数据,覆盖写到文件中
        """
        # 1.得到所有value对应的列表
        student_list = self.student_dict.values()
        # 2.打开文件,以只写的方法打开文件
        f = open("student.txt","w",encoding="utf-8")

        # 3.遍历列表,每个元素都是一个对象
        for student in student_list:

            # 4.在循环中,得到学生对象的学号,姓名,分数,组成一个字符串
            line = student.id + "," + student.name + "," + student.score
            # 5.把这个字符串写入到文件中
            f.write(line + "\n")
            pass
        # 6.循环结束后,关闭文件
        f.close()

        pass

    def file_to_dict(self):

        """
        读取文件中的数据,一行一行的读取
        从读到的一行数据中解析出学号,姓名,分数,创建一个学生对象
        把对象作为value,把学号作为key,添加到字典中
        """
        # 1.以只读的方式打开文件
        f = open("student.txt","r",encoding="utf-8")
        # 2.循环着读取文件，一行读一行
        while True:
            line = f.readlines()
            if line != "":
                # 去掉最后的换行符
                line = line[0:len(line)-1]
                # 3.在循环里面，从读到的一行数据中解析出学号，姓名，分数
                infos = line.split(",")
                id = infos[0]
                name = infos[1]
                score = infos[2]
                s = Student(id,name,score)
                # 5.把对象作为value，把学号作为key，添加到字典中
                self.student_dict[id] = s
                pass

            else:
                # 如果本次没有读到数据，表示 数据已经读完了，应该终止循环
                break
                pass

            pass


        pass


    pass



