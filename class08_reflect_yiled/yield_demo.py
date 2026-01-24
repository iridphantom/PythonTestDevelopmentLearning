"""
    Yield关键字：
        yield是Python中的特殊关键字，是一个生成器
        迭代，其实就是循环的概念：
            1. 可迭代对象：其实就是可以通过循环来实现操作的对象。
            2. 迭代器：属于可迭代对象，一次只能取一个值，一直取到全部取完为止（或者说程序终结为止）。
            3. 生成器：属于特殊的迭代器。它只能通过yield关键字来定义。
                yield关键字只能用于函数 / 方法之中
                yield类似于函数中的return关键字，都属于返回值的操作行为。
                    return：返回值后函数彻底终止
                    yield：返回值后函数暂停，保持当前状态等待下次调用

"""

"""
    可迭代对象：
"""
a = 'uhygagkhbkdsayuik'

# b = 2   # int不是可迭代对象
# for i in a:
#     print(i)


"""
    迭代器:例如readline()就是一个标准的迭代器
"""
# 自定义迭代器:只有可迭代对象才能被迭代，自定义迭代器需要实现__iter__()和__next__()方法
# print(type(a))
# b = iter(a)    # 将str类型的a变量转为迭代器  类似于强转的写法
# # print(type(b))  # <class 'str_ascii_iterator'>
# # for i in b: # 遍历迭代器中的每个字符并逐个打印输出。
# #     print(i)
#
#
# """
#     迭代器的取值操作————next()。
#     next读取迭代器中的值，每次读取一个值，光标移至下一行，一直到读完为止或者程序终结，类似于readline()
# """
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


"""
    yield关键字生成生成器
"""
# file = open(r'D:\Project\Python\hcc_python_class\class07_file\paper1.txt', mode='r', encoding='utf-8')
# def fun1():
#     for line in file.readlines():
#         # return line # ⚠️遇到第一行就返回并终止函数，函数执行流程就此结束，不再继续后续的循环
#         yield line



"""
    生成器
"""

def fun2():
    for i in range(0, 10):
        yield i

num = fun2()    # 调用fun2()函数，获取生成器

print(num)  # 这里的 print(num) 是用来打印生成器对象本身的信息，而不是生成器产生的值
"""
    <generator object fun2 at 0x0000020EA5EA0E80>
    generator object：这是一个生成器对象
    fun2：该生成器来源于 fun2 函数
    at 0x0000020EA5EA0E80：生成器对象在内存中的地址
"""

print(next(num))    # 输出生成器产生的具体值（如 0, 1, 2...）
print(next(num))    # 1


# -------------------------------------------------------------------------------
"""
测试在大体上分为三个行为
    1. 测试初始化
    2. 执行测试
    3. 测试收尾结束————避免重新进行测试的时候，遇到数据相同的问题。比如说昨天进行注册操作，今天再进一次注册操作，而测试数据是一样的，这样就会报错，因此需要进行数据销毁
"""
def fun3():
    # 测试前
    print('测试的初始化')
    print('测试数据的生成')
    data = '测试数据'

    # 将测试数据应用与实际的测试之中
    yield data  # 将数据提取。交由实际的测试用于执行，执行完毕之后进行收尾工作

    # 测试收尾
    print('整个测试结束。资源释放正常')


print('---测试开始---')
te = fun3()
print('---测试执行---')
print(next(te))
print('---测试结束---')
print(next(te))