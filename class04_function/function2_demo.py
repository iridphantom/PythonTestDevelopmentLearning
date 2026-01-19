"""
    匿名函数：
        官方明确定义，不推荐所有人使用的一种方式。但是官方一直都支持这种方式。
        懒人版函数。只有极少数情况下会用到。不想写标准函数的时候的替代品。
        匿名函数通过关键字lambda来实现

    递归函数：
        本质上就是函数调用它自己
        因为在重复调用自己的过程中，整个函数的逻辑处理会变得越来越复杂，会关联死循环和循环的概念。
        递归本质上就是循环。所以我们需要在递归的过程中设置最终的跳出条件。从而避免递归的死循环。
"""
# 匿名函数示例：

a = lambda b: b+10  # 定义了一个匿名函数，要求传入一个参数b，执行b+10的操作
print(a(10))    # 10

# 对应的完整版：
# def a(b):
#     b = b + 100
#     return b


# ---------------------------------
# 递归示例
def recursive(n):
    num = n
    for i in range(1, n):
        num = num * i
    return num

print(recursive(5))
'''
    num = 5
    for i in range(1,5):
        num = num * i

    num = 5*1 = 5
    num = 5*2 = 10
    num = 10*3 = 30
    num = 30*4 = 120
'''

# 上面的递归版本：添加了推出条件
def mul_plus(n):
    if n == 1:  # 设置递归的退出条件，避免递归死循环
        return 1
    else:
        num = n * mul_plus(n - 1)
    return num

print(mul_plus(10))
'''
    num = 10 * mul_plus(9)
    num = 9 * mul_plus(8)
    num = 8 * mul_plus(7)
    num = 7 * mul_plus(6)
    .....
    num = 2 * mul_plus(1)
    重新返回：
    num = 2 * 1
    num = 3 * 3
    num = 4 * 9
    num = 5 * 36
    .....
    num = 10 * 362880    
    所以num = 3628800
'''