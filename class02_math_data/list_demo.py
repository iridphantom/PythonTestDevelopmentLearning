'''
    list和dictionary的相关操作
'''

# list
a = [1, 2, 3, 4, 5, 6, 7]
# 通过下标获取元素，下标从0开始。
print(a[0]) # 1
print(a[1:]) #从下标1开始，往后读取所有的元素 [2, 3, 4, 5, 6, 7]
print(a[-1]) # 从后往前读。 7
print(a[:5]) # 从0开始读取到第五个元素。这里的5代表终止符。[1, 2, 3, 4, 5]
print(a[1:5])   # 从1开始读取到第五个元素

# 在原有的list上，在末尾添加元素
print("添加前：", a)
a.append('asd')
print("添加后：", a)

# 删除list中已有的元素
# 1.基于下标删除：
a.pop(-1)
print(a)
# 基于元素值删除
a.remove(5)
print(a)


# 获取list的长度
print(len(a))

# 排序：确保元素统一为同一个数据类型
b = [1, 15, 100, 85, 20, 19]
print(b)
# b.sort()    # sort排序会直接影响原有的b的元素顺序
print(sorted(b))    # sorted排序不会影响原有的b的元素顺序。 [1, 15, 19, 20, 85, 100]
print(b)    # [1, 15, 100, 85, 20, 19]


# ----------------------------------------------
# 字典类型
a = {
    'name': '张三',
    'age': 18
}

# 创建空字典
# b = {}  # 创建空字典。set也是基于{}创建，但是Python默认{}创建的是空字典，而非set
# c = dict()  # 创建空字典

# 通过key获取value值
print(a['name'])    # 基于name这个key，获取到对应的value值

# 删除指定的键值对：pop()
# print(a)
# a.pop('name')   # 基于name这个key，删除对应的键值对
# print(a)

# 清空整个字典的所有内容：.clear()
# print(a)
# a.clear()   # 全部内容清空，不再剩余任何东西
# print(a)

# 获取字典的所有key
print(a.keys()) # dict_keys(['name', 'age'])

# 获取字典的所有value
print(a.values())   # dict_values(['张三', 18])

# 获取字典中所有的键值对
print(a.items())    # dict_items([('name', '张三'), ('age', 18)])

# 基于循环来获取所有的键值对，并进行操作
for key,value in a.items():
    print(key)
    print(value)











