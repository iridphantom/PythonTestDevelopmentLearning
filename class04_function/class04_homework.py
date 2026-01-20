"""
    1. 熟悉*args和**kwargs的传参方式
    2. 自行练习递归的实现。也可以在网上搜递归的编程题自己熟悉。
"""



"""
    ## 函数对比分析

这两个函数**不是完全等价的**，虽然它们最终输出相同，但在参数传递机制上有本质区别：

### [my_function](file://D:\Project\Python\hcc_python_class\class04_function\class04_homework.py#L5-L7) 使用 `*args`
- **参数接收方式**：`*args` 直接接收可变数量的位置参数
- **[args](file:///D:/Project/Python/hcc_python_class/class04_function/class04_homework.py#L7-L8)** 是一个元组，包含所有传入的参数
- **解包操作**：`*args` 将元组中的元素逐一展开输出

### [my_function2](file://D:\Project\Python\hcc_python_class\class04_function\class04_homework.py#L13-L15) 接收单个参数
- **参数接收方式**：接收一个单一参数（在例子中传入的是元组）
- **参数类型**：`[args](file:///D:/Project/Python/hcc_python_class/class04_function/class04_homework.py#L7-L8)` 就是传入的那个元组对象本身
- **解包操作**：`*args` 同样执行解包，但这里的 [args](file:///D:/Project/Python/hcc_python_class/class04_function/class04_homework.py#L7-L8) 是预先包装好的元组

## 执行过程对比

### [my_function('asd', 1, "2", 3)](file://D:\Project\Python\hcc_python_class\class04_function\class04_homework.py#L5-L7)
1. 参数 `'asd'`, `1`, `"2"`, `3` 被自动收集到元组中
2. [args](file:///D:/Project/Python/hcc_python_class/class04_function/class04_homework.py#L7-L8) 变成 [('asd', 1, '2', 3)](file://D:\Project\Python\hcc_python_class\class02_math_data\list_demo.py#L0-L86)
3. 第一行打印：[('asd', 1, '2', 3)](file://D:\Project\Python\hcc_python_class\class02_math_data\list_demo.py#L0-L86)
4. 第二行打印：`asd 1 2 3`（解包后逐个输出）

### [my_function2(tuple2)](file://D:\Project\Python\hcc_python_class\class04_function\class04_homework.py#L13-L15)
1. 整个元组 [('asd', 1, "2", 3)](file://D:\Project\Python\hcc_python_class\class02_math_data\list_demo.py#L0-L86) 作为单个参数传入
2. [args](file:///D:/Project/Python/hcc_python_class/class04_function/class04_homework.py#L7-L8) 就是 [('asd', 1, '2', 3)](file://D:\Project\Python\hcc_python_class\class02_math_data\list_demo.py#L0-L86)
3. 输出结果与上面相同

## 关键区别

**调用方式不同**：
- `my_function` 直接接受多个独立参数
- `my_function2` 需要先将参数打包成容器再传入

**设计用途不同**：
- `my_function` 适用于不知道参数数量的情况
- `my_function2` 适用于参数已经组织在容器中的情况
"""


def my_function(*args):
    print(args)
    print(*args)

my_function('asd', 1, "2", 3)



def my_function2(args):
    print(args)
    print(*args)

tuple2 = ('asd', 1, "2", 3)
my_function2(tuple2)

# --------------------------------------------------------
# 给我一个递归函数的题目：
# 输入一个数字，求这个数字的阶乘。(阶乘是指从1到n的所有正整数的乘积。5! = 1 × 2 × 3 × 4 × 5 = 120
def recursive(a):
    if a == 1:
        return 1
    else:
        return a * recursive(a - 1)

print(recursive(4))



