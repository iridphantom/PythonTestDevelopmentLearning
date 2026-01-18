"""
    while循环：
        while 条件:
            while循环体    # 只要条件为True，则一直循环，一直到条件为False为止

    while循环是很可能出现死循环的。也就是循环会一直都执行下去，不会结束。为了避免死循环。我们在调用while执行循环时，需要设置退出条件

    虽然在循环的过程中，我们需要避免死循环。但很多时候我们也需要死循环来帮助我们解决程序逻辑。所以一定记得定义退出的条件。
"""

# while循环示例
# a = 0
# while a < 10:
#     print(a)
#     a += 2

# -----------------------------------

# while死循环示例：一定记得设置退出条件避免死循环的产生。
# a = 0
# while True:
#     print('while死循环')
#     if a > 10:
#         break
#     a += 5
#
# print('while后续逻辑')

# -----------------------------------

# 通过死循环来完善之前所写的小游戏。
content = '''
    请输入你想要做的事情：
        1. 上课
        2. 玩手机
        3. 玩游戏
        4. 睡觉
        5. 退出
'''
while True:
    value = int(input(content))  # input()表示支持用户在控制台进行输入操作。可以把用户的输入内容获取在程序之中

    if value == 1:
        print('好好学习，天天向上')
        value = int(input('''
            请输入你想要学的内容：
                1. 物理
                2. 数学
                3. 计算机
        '''))
        if value == 1:
            print('学好物理')
        elif value == 2:
            print('学好数学')
        elif value == 3:
            print('学好计算机')
    elif value == 2:
        print('原神启动')
    elif value == 3:
        print('CS2启动')
    elif value == 4:
        print('做个好梦')
    elif value == 5:
        print('这次结束，期待下次见面')
        break   # break终止整个循环，是最有效的终止死循环的手段
