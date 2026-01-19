"""
    return关键字：
        判断函数是否有值，只看是否有return，其余都没有任何意义。print只是控制台打印，并不会生成数据返回。
        函数默认没有返回值。默认为None
        return执行后，函数会停止运行，后续代码不再执行。所以return一般放在函数的末尾。

    global关键字:
        1. 变量的作用域：每一个变量在定义的时候，都有自己的作用域，也就是有效范围。
        2. 在Python中，默认不支持在函数中修改函数外的全局变量。如果实在想要修改，可以通过global关键字实现。
        3. 如果需要用global，则一定是在函数的第一行声明，避免报错风险。
"""

# return示例
def no_return():
    print('这是没有return的函数')

def have_return():
    print('这是有return的函数')
    return 100

# a = no_return() # 函数没有返回值时，不需要赋值给变量。
print(no_return())

b = have_return()
print(f"b:{b}") # 100

# -----------------------------
def return1():
    print(1 + 50)   # 控制台输出和有没有值没有一点关系。

print(return1())



# global-----------------------------
a = 10

def demo_plus1():
    a = 100    # 在函数内重新定义了一个新的变量a，而不是用的全局变量a。作用域只在该函数内
    print(a)

demo_plus1()
print(a)

print("-----global关键字：-----")

def demo_plus2():
    global a  # global关键字声明以后，a就变成可修改的全局变量。
    a = 100
    print(a)
print(f"调用前a的值：{a}")
demo_plus2()
print(f"调用后a的值：{a}")