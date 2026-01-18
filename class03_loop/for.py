"""
    for循环语法结构：

    for 循环条件
        循环代码块

    提前终止循环的方式：通过break和continue来实现
    循环在执行的过程中可能会执行非常多次。实际程序在运行时可能不需要执行那么多次，如果要提前结束循环，则调用关键字实现
    break：终止整个循环。后续的所有待执行的循环次数都不再执行。
    continue：终止本次循环，直接进入下一次循环
"""

# # for循环示例
# li = [1, 2, 3, 4, 5, 6, 7]
# # 基于for循环来实现元素的读取。
# for i in li:  # i表示临时变量，用于在循环过程中临时存在，当做元素的变量。只在循环中有效
#     print(i)
#
# print(i)    # 循环外基本不会再使用临时变量。


# -----------------------------------

# # for循环的基本结构：用于定义循环次数的最简单的方式
# for i in range(0, 10):  # range()就是生成一个临时的list，0表示起始位，10表示终止位，所以值为0-9
#     print(i)

# -----------------------------------

# # for循环的计数
# a = 0
# for i in range(0, 10):
#     print(a)
#     a += 1
#
# print("最终的运行结果：" + str(a))

# -----------------------------------

# # 字典的循环
# dict1 = {
#     'name': '张三',
#     'age': 18,
#     'sex': '男'
# }
# # 多个值存在的情况下，临时变量的赋值和循环执行。临时变量赋值是依次执行的。
# for key, value in dict1.items():  # key和value都属于临时变量。因为a.items()会生成两个不同的值。
#     print(f'字典中的key为{key}，value为{value}')
#
# # 打印keys
# for key in dict1.keys():
#     print(f'字典中的key为{key}')
#
# # 打印value
# for value in dict1.values():
#     print(f'字典中的value为{value}')

# -----------------------------------

# # for循环的嵌套：在子循环全部结束之后，才会进入到新一轮的外循环。
# li = []
# for i in range(0, 5):  # 执行5次循环
#     li1 = []  # 生成新的list
#     for j in range(0, 3):  # 执行3次循环
#         li1.append(j)  # 将子循环的数据添加至li1之中
#     li.append(li1)  # 将li1添加至li中
# print(li)

# -----------------------------------

# break continue示例
for i in range(0, 999):
    if i == 3:
        continue    # 终止本次循环，进入下一次循环
    elif i == 5:
        break      # 结束整个循环
    print(i)