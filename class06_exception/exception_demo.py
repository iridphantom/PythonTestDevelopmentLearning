"""
    try...except...语法应用：
        语法结构：
            try:
                try代码块  # 正常代码，但是在运行时可能会产生异常，所以放在try之中。
            except:
                except代码块   # 当try代码块出现报错时，则立即进入except之中，执行此处代码。就是用于处理异常

        程序一旦报错，会在报错的位置直接终止运行，在控制台抛出异常信息。但是加上"try...except..."后，当try中的代码出现错误后，程序不会终止运行。
        我们会将可能出错的代码放在try之中，如果出错则进入except进行异常处理，否则不会进入except，程序正常运行。
        try...except...是用于处理程序中的异常情况的。所以当出现异常时，因为有try的存在，所以程序默认错误已经被处理了，所以不会再继续报错。
        try...except本质其实和if...else没有太大区别。只是说try语句是专门用于处理异常的。而if语句可以适应的场景更多。
        try...except是一套完整的代码结构，无法独立存在。try语句是可以嵌套的。


    Exception对象：
        Exception时所有异常和错误的爹，Exception继承于BaseException
        因此所有的异常和错误，都是继承于BaseException类来实现的。
        所有的异常和错误，都有独属于自己的类（例如ValueError、ZeroDivisionError...）。而except语法可以捕获指定的异常和错误。
        except可以存在多个，用于处理多个不同的异常
        Exception对象还可以自定义异常类。实现自定义的异常

    else...finally语法结构：
        try:
            可能出错的代码块
        except:
            出错后的处理手段
        else:
            如果未出错，则进入此处
        finally:
            无论是否出错，最终都会执行

        finally是在try模块中非常常用的关键字。因为无论是否报错都会执行的代码块。所以常见于释放资源相关操作
        如果需要做代码关联，则会应用到else，用于关联try之中的代码，作为逻辑的延续。而其余场景很少使用
        else...finally一定是关联try语句块来使用的。


    raise关键字：用于手动抛出异常
        当遇到我们不想（不能）处理的异常时，可以对其进行抛出的操作。让程序产生异常，从而交由后续调用的人去解决。
        raise抛出异常后，异常依旧存在，因此它不是解决异常的手段。它相当于我们制造了一个异常，或者对已经存在的异常进行抛出的处理，所以异常依旧存在。
        raise可以抛出指定异常，或者不加异常直接抛出,则会提示RuntimeError


    Traceback模块：是一个Python官方库。不需要安装，直接导入使用即可。
        所有的异常信息，都是基于Traceback来显示在控制台之中的。
        当我们使用了try...except...之后，就不会在控制台中显示任何异常信息了
        如果调用Traceback模块，就可以在try语句块中，显示详细的报错信息。
        调用traceback.print_exc()实现异常信息的详细内容在控制台中打印

整个异常处理的一节课，除去最基本的异常处理行为之外，更多需要懂得如何去控制异常，从而控制你的代码逻辑。

"""
import traceback

# try...except...示例
try:
    print(1)
    1 / 0   # 运行时产生异常，则进入except代码块
    print(2)    # 产生异常->跳过后续的代码，直接执行except代码块
except:
    print("错误")
print(123123)

# -------------------------------------------------------

"""
    Exception
"""

try:
    print(1)
    1 / 0
except Exception as e:  # Exception表示任意异常。 as表示起别名： e表示别名。
    print(e)    # 打印捕获的异常信息。    division by zero
    # print(Exception)    # 打印Exception类的信息。  <class 'Exception'>
    print(1)
except ValueError as ve:
    print(ve)
    print(2)
except ZeroDivisionError as zde:
    print(zde)
    print(3)



# -------------------------------------------------------
# 自定义一个异常类:通过继承Exception类
class MyException(Exception):
    pass
print(MyException)  # <class '__main__.MyException'>


# -------------------------------------------------------
"""
    else...finally语法示例
"""

# else...finally语法示例
try:
    num = int(input("请输入一个数字："))
    result = 10 / num
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以零！")
else:
    print(f"计算结果是：{result}")
    print("计算成功！")
finally:
    print("无论是否有异常，都会执行这里")



# -------------------------------------------------------
"""
    raise关键字
"""

try:
    1 / 0
except:
    print("错误")
    raise   # 将已产生的异常直接抛出。


try:
    1 / 0
except Exception:
    raise ValueError  # 将已有的异常继续抛出，不做处理。此处会生成两个异常
except ZeroDivisionError:
    raise  # 将已产生的异常直接抛出。


# -------------------------------------------------------
"""
    Traceback
"""
# Traceback示例
try:
    1 / 0
except ZeroDivisionError as e:
    # print(e)
    traceback.print_exc()

print(123)

