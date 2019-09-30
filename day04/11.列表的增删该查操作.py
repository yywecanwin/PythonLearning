# -*- coding: utf-8 -*-
# author：yaoyao time:2019/10/1

name_list = ["yao",'is','a','good','man']

#1.向列表中添加一个元素
# append(数据)：在列表的最后添加一个元素
name_list.append("nice")
print(name_list) # ['yao', 'is', 'a', 'good', 'man', 'nice']

#在指定的索引处插入一个元素
name_list.insert(2,"hello")
print(name_list) # ['yao', 'is', 'hello', 'a', 'good', 'man', 'nice']

#继承：把另一个容器中的元素添加自己的容器中
list1 = [10,20,"hh"]
name_list.extend(list1)
print(name_list) # ['yao', 'is', 'hello', 'a', 'good', 'man', 'nice']
name_list.extend("hello")
print(name_list) # ['yao', 'is', 'hello', 'a', 'good', 'man', 'nice', 10, 20, 'hh']

#修改方法
list2 = [10, 3.14, "hello", True]
#根据索引得到列表中的元素：列表名[索引]
print(list2[0])
print(list2[2])

# 修改指定位置的元素：列表名[索引]  = 新的值
list2.remove("hello")
print(list2) # [10, 3.14, True]

#删除指定索引的元素，返回被删除的元素
result = list2.pop(1)
print(result) # 3.14
print(list2) # [10, True]

# pop方法中没有写索引,默认删除最后一个元素
list2.pop()
print(list2) # [10]

list2.append("python")
print(list2) # [10, 'python']
list2.pop()
print(list2) # [10]

#把列表中的元素全部删除，清空
list2.clear()
print(list2) # []
