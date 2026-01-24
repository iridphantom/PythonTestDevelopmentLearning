"""
    反射机制：
        1. getattr()方法，是所有反射机制的方法中使用频率最高的一种方法
        通过指定的字符串来获取目标模块中所拥有的属性或者方法。其实就是对属性或者方法的另一种调用模式。
        主要包含两个参数：
            ①. 目标模块：类名称 / 实例化对象
            ②. 名称：是字符串类型，基于名称来实现对目标模块指定的属性、方法进行调用。
        该方法主要是用于获取目标对象的属性或者方法。如果是获取方法，记得在代码末尾添加()
        对于不存在的属性或者方法，调用时会直接报错。可以通过try...except来实现。

        2. setattr()设置目标对象的属性：通过此方法可以对目标对象新增属性 / 修改自己已有的属性值
            ①. 对于已存在的属性，则为修改
            ②. 对于不存在的属性，则为新增
            该方法只能对属性进行操作，对类方法无效

        3. hasattr()：判断属性是否存在。存在返回True，否则返回False

        4. delattr()：删除指定的属性。
            该方法只能对类使用，而无法对实例化对象使用。


"""
from class08_reflect_yiled.person import Person

"""
    getattr()示例：
"""
# 常规调用方法
p1 = Person()
print(p1.name)
p1.eat()

# 基于反射机制实现调用
print(f"基于反射机制实现调用：{getattr(p1, 'name')}")  # 相当于p1.name


"""
    通过for循环实现所有内容的属性获取：
    # 遍历列表中的每个元素，并通过getattr动态获取p1对象对应的属性或方法
    # 这种方式可以减少重复的if-else或switch-case逻辑，提高代码简洁性
    li = [1,2,3,4,5]
    for i in li:
        getattr(p1, i)  # 可以极大节省代码逻辑
"""

# # getattr()实现方法调用
# print(getattr(p1, 'eat'))   # <bound method Person.eat of <class08_reflect_yiled.person.Person object at 0x0000016457DC9250>> 绑定了Person.eat()这个方法，是基于Person object实现的
# getattr(p1, 'eat')()    # 调用方法：在后面需要加括号。相当于调用p1.eat()
#
# getattr(p1, 'sleep')('8小时') # 传入参数：在括号中添加参数
#
# print(getattr(Person, 'name'))  # 通过类名调用属性



"""
    # setattr() 示例
"""
print('--------------setattr()示例--------------')

# print(f"修改前的值：{getattr(p1, 'name')}")   # 修改前的值：张三
# setattr(p1, 'name', '王五')
# print(f"修改后的值：{getattr(p1, 'name')}")   # 修改后的值：王五

# 新增不存在的属性：
# setattr(p1, 'like', '打羽毛球')
# print(f"新增的属性：{getattr(p1, 'like')}")   # 新增的属性：打羽毛球

# 修改类属性
setattr(Person, 'name', '李四')
print(Person.name)
print(p1.name)


"""
    # hasattr() 示例
"""
print(hasattr(p1, 'name'))  # True
print(hasattr(p1, 'like'))  # False

print(hasattr(p1, 'play'))   # 也可以判断方法是否存在  # False


"""
    # delattr() 示例
"""
# 删除属性：
# delattr(p1, 'name') # 报错，因为该方法只能对类使用，而无法对实例化对象使用。：AttributeError: 'Person' object has no attribute 'name'
# delattr(Person, 'name')  # 删除类中存在的属性。这行代码之后，类中不再有name属性
print(p1.name)  # AttributeError: 'Person' object has no attribute 'name'

# 删除方法
delattr(Person, 'drink')  # 删除类中的方法名称，该方法将继续存在，但无法被调用
p1.drink()    # 调用方法失败是因为方法名称找不到，而不是方法被删除了。  AttributeError: 'Person' object has no attribute 'drink'
# 在类之中创建方法的时候,方法名会变成类的一个属性.这个属性是绑定方法名称存在的-^