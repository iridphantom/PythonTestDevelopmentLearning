"""
    pymysql实现数据库的操作：
        1. 查询（最常用）
        2. 增删改
    pymysql操作流程：
        1. 连接数据库，需要获取到数据库的对应配置信息
        2. 创建游标：数据库的所有内容都是基于游标来获取的。（游标：
        3. 操作数据库：
            1. 查询：获取结果的方式就是基于游标的方法来实现。对所有的数据结果都可以通过游标进行获取和控制。
            2. 增删改：
                只要关联到原有表格数据的变动，则一定需要commit()才能够生效，否则所有修改都属于无效。
                commit()提交修改；
                rollback()回滚，对未提交的修改操作可以直接撤回。
"""
import pymysql

from class11_mysql.read_conf import read

# 链接数据库所需的配置信息
# db_info = {
#     'host': '127.0.0.1',  # 数据库的ip地址
#     'port': 3306,  # 数据库端口号
#     'user': 'root',  # 账号
#     'password': '201837',  # 密码
#     'database': 'takeaway'  # 连接的数据库名称
# }
# # 基于配置信息，连接数据库
# conn = pymysql.connect(**db_info)   # 定值不定长传参方式。**db_info表示将字典中的内容进行解包，将字典中的内容作为参数进行传递。

conn = pymysql.connect(**read('ONLINE_ENV'))  # 定值不定长传参方式。

# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 将数据结果以字典的格式进行返回。

"""
# 操作数据库：实现查询功能
# 定义sql
sql = 'select * from user'
# 调用sql进行mysql的操作
cursor.execute(sql)

# sql执行后，想要获取所有的结果，都需要使用基于cursor的fetch*()方法来实现
results = cursor.fetchall() # 获取所有的查询结果，并返回为list数据类型
for result in results:
    print(result)
    
print("——————————————————————————————————————————————")
"""

# 一行一行读取：cursor.fetchone()-------------------------------------------------
"""
sql = 'select * from user'
cursor.execute(sql)
result = cursor.fetchone()  # 类似于readline，一次获取一行，一直到程序结束，或者全部获取完
print(result)

print("——————————————————————————————————————————————")
"""


# 获取指定长度行：cursor.fetchmany(你想要几行)-------------------------------------------------
"""
sql = 'select * from user'
cursor.execute(sql)

results = cursor.fetchmany(4)   # many就是想要获取几个就指定获取数量即可。游标依旧自行下移到获取的最后一行。
for result in results:
    print(result)

# 依据上面的结果，继续获取
result = cursor.fetchone()  # 类似于readline，一次获取一行，一直到程序结束，或者全部获取完
print(result)

print("——————————————————————————————————————————————")
"""


# 游标的操作-------------------------------------------------
"""
print("游标的操作 游标的操作 游标的操作")
sql = 'select * from user'
cursor.execute(sql)
result = cursor.fetchone()  # 类似于readline，一次获取一行，一直到程序结束，或者全部获取完
print(f"第一行：{result}")
# 1. 游标的前移：relative & absolute。scroll的默认方法是relative。
# cursor.scroll(1, mode='relative')   # # 基于光标当前的位置，向下移动指定行数，再进行后续操作。 这里向下移动了1行
# cursor.scroll(3, mode='absolute')    # 永远都是从第一行向下移动，不考虑光标当前所在位置。 这里是从第1行开始，向下移动3行

# 2. 游标的后移
# cursor.scroll(-1)   # 向上移动1行

print(cursor.fetchone())

print("——————————————————————————————————————————————")
"""


# 数据库的增删改-------------------------------------------------
try:
    sql = 'insert into user(username, password) values("pysql", "123456")'
    cursor.execute(sql)
    conn.commit()   # 二次确认sql的修改行为
except Exception as e:
    conn.rollback()  # 回滚操作，取消之前所执行的所有对应修改操作行为，但是对已经commit的行为无效
finally:
    # 关闭游标和数据库连接。
    # 数据库的所有操作，都是基于连接来完成的。连接池-->可以理解为钥匙库，连接时候会从钥匙库获取钥匙，使用完毕之后，会放回钥匙库。
    # 当大批量的请求数据库时，连接数满了后，剩下未连接的在排队等待，直到有连接可用。若长时间未能连接，则会报错。
    cursor.close()
    conn.close()
