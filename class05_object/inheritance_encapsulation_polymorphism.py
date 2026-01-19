"""
    面向对象编程的三大要素：
        1. 继承：子类继承父类。   主要目的是：简化代码。
            子类可以将父类中【所有已有的可被继承的内容】，全部都继承在子类中。
            继承的方式：
                子类类名(父类类名)
            不可被继承的就是私有属性和私有方法，通过__来定义。如果父类之间存在有相同的属性或者方法时，则根据继承的顺序，从左至右来确定最终继承的内容，先继承谁就是谁的值。
            可以多继承：一个子类可以继承于多个父类。
            多继承时，不同的父类，用,进行分割。

        2. 封装：封装是一种概念，不是某种特定的代码格式。
            为了降低代码的冗余，提升代码复用性的一种形式。

        3. 多态：程序的多种形态
            一个事务是具备有多种不同的形态。在类的属性和方法上可以进行多态的定义。
            共有两种概念：
             ①.方法的重写：将夫类之中已被子类所继承的方法，在子类中进行定义。柚子，不同对象的同一个方法，可以实现不同的效果
             ②.方法的重载（Python不支持）：同一个方法，基于定义的参数数量不同，来实现不同的效果。

"""

"""
    继承
"""

class Father:   # 父类1
    # 构造方法
    def __init__(self,  name):
        self.name = name

    car = "BMW 530i"
    house = "500平大别野"
    money = "100W U$"
    __browser_history = "劲爆内容"  # __表示私有属性，无法被继承。

    def view_history(self):   # __view_history中的__表示私有方法，无法被继承。
        print(f"{self.name}在查看浏览器历史记录")


class Godfather:    # 父类2
    def __init__(self, name):
        self.name = name

    car = "BMW M5"
    house = "10000平大庄园"
    money = "500W U$"


# 子类，继承于父类
class Son(Father):  # 子类
    def son_function(self):
        print("子类自己的方法")


# son = Son("老爹")
# print(son.car)
# # print(son.__browser_history)
# # son.__view_history()


# 多继承
# class Grandson(Godfather, Father):  # 继承顺序：从左往右。
#     pass
#
# son2 = Grandson("asd")
# print(son2.car)



"""
    多态
"""
son3 = Son("老爹")
son3.view_history()

