"""
    if判断：
        基本语法结构：
            if 条件1: # 如果条件1为True，则执行if代码，所以条件1可以是一个表达式
                if代码块
            elif 条件2:   # 如果条件2为True，则执行elif代码
                elif代码块
            else:   # 如果是其他条件，则执行else
                else代码块
    所有的判断条件只会执行其中一条。
    所有的判断是可以有多种的，通过添加elif来增加多的判断条件。同时，elif是可以有无限多个的。实际编写程序时，不会写非常多的elif
    elif必须存在于if...else语法结构之中，无法单独存在。
    else也无法单独存在。else也可以没有。根据实际编写程序的情况来定义我们的判断分支。
    if...elif...else三者的搭配根据实际情况灵活选择即可。

"""

# # if代码示例
# a = 1
# if a == 10:
#     print('这是if代码块')
# elif a == 1:
#     print('这是elif代码块')
# else:   # else一定是放在整个判断最后的。
#     print('这是else代码块')

# -----------------------------------

# # if执行逻辑：每一个if都是独立的语句。三个判断不管条件是否满足，都会执行。
# a = 100
# if a == 100:
#     print('这是第一个判断')
# if a == 50:
#     print('这是第二个判断')
# if a == 5:
#     print('这是第三个判断')

# -----------------------------------

# if判断的实操
content = '''
    请输入你想要做的事情：
        1. 上课
        2. 玩手机
        3. 玩游戏
        4. 睡觉
        5. 退出
'''

value = int(input(content))  # input()表示支持用户在控制台进行输入操作。可以把用户的输入内容获取在程序之中
# print(type(value))
if value == 1:
    print('好好学习，天天向上')
    content = '''
        请输入你想要学的内容：
            1. 物理
            2. 数学
            3. 计算机
    '''
    value = int(input(content))
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