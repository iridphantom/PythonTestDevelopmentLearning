'''
    str类型的操作行为
'''

# 占位符操作：在已有str的内容基础上，在不修改原有格式的情况下，来将新的内容添加进去
name = '周杰伦'
a = f'我喜欢听{name}的歌，他的歌让我找到青春。'  # 占位符的使用，一定记得在字符串前添加f
print(a)

# 多行输出：一般情况下多行输出会保留原有的格式。一般是使用三对引号来实现，也就是多行注释。
a = '''
        静夜思
            ——李白-唐
        床前明月光，
        疑似地上霜。
        举头望明月，
        低头思故乡。
'''
print(a)


# 编码操作：从文件中获取数据的时候，如果编码格式不对，则会出现乱码。传统中文的编码格式是utf-8。
str1 = '李白'
print(str1) # 李白
str2 = str1.encode(encoding='GBK')  # 修改了默认的编码格式
print(str2) # 乱码
print(str2.decode(encoding='GBK'))  # 解码操作行为，基于指定的编码格式对内容进行解码。  # 李白


# 大小写转换
a = 'Time To Say Goodbye'
# 全部大写
print(a.upper())
# 全部小写
print(a.lower())
# 首字母大写（第一个字母）
print(a.capitalize())

# 去除字符串首尾的指定字符：strip
# print(a.strip())  # 默认去除首尾的空格
# print(a.strip('T'))  # 也可以指定需要进行首尾去除的字符串

# 字符串的分割：split
print(a.split())    # 默认以空格进行分割，将他们组合成list。['Time', 'To', 'Say', 'Goodbye']
a = '2a1abacad'
print(a.split('a')) # 指定进行分割的字符串。['2', '1', 'b', 'c', 'd']
print(a.split('a', 3)) # 基于指定字符串进行字符串的分割。还可以定义分割最大次数。


# 字符串的替换：可以实现对字符串进行替换，删除，以及指定次数的相关操作
a = 'wo shi zhang san'
print(a.replace('zhang','Z'))
print(a.replace('zhang',''))  # 删除huang
print(a.replace('a', '1', 1))   # 替换a，只替换一次

# 字符串的拼接处理
a = 'wo shi zhang san'
a = a.split()   # 将字符串进行分割，将字符串进行list的存储。['wo', 'shi', 'zhang', 'san']
b = 0
for i in a:
    a[b] = i.upper()
    b+=1
c = ' '.join(a)  # join实现字符串的拼接，将整个a的list元素，基于' '来进行拼接。可以将整个list的所有元素一次性按照规则全部拼接成一个完整字符串
print(c)    # WO SHI ZHANG SAN

































