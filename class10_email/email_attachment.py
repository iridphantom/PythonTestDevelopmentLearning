'''
    发送带有附件的邮件：
        主要解决的是在发送邮件时需要携带附件的场景。需要对附件部分的代码进行额外的编写。
        附件发送的代码，如果说参数配置出现有问题，则附件是无法正常解析的。
'''

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 定义邮箱的相关信息
sender = '2783523607@qq.com'
receiver = '483983530@qq.com'
pass_code = 'uqmypuziquxmdgdc'

# 链接邮箱服务
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)

# 发送带有附件的文件：
content = '这是邮件的正文 这是邮件的正文 这是邮件的正文'
cont = MIMEText(content, 'plain', 'utf-8')  # 正文的发送

# 定义附件内容
# 添加一个附件
with open('C:/Users/1/Pictures/111.jpg', 'rb') as file:
    file_data = file.read()

# 使用MIMEApplication处理二进制附件
att = MIMEApplication(file_data)
att.add_header('Content-Disposition', 'attachment', filename='ROG.jpg')

# 将附件添加到邮件中
email = MIMEMultipart()  # 创建一个MIMEMultipart对象，用于添加附件
email.attach(att)      # 将附件添加进邮件之中
email.attach(cont)     # 将正文添加进邮件之中

# 将邮件的发件人与收件人进行定义
email['From'] = sender  # 定义发件人
email['To'] = receiver  # 定义收件人
email['Subject'] = Header('这个是带有附件的邮件', 'utf-8')  # 设置邮件的主题

# 发送邮件
conn.login(sender, pass_code)  # 基于发件人账号与授权码进行smtp服务的登录
conn.sendmail(sender, receiver, email.as_string())  # 将定义好的邮件进行发送

# 邮箱服务关闭
conn.close()

"""
    多个附件发送的代码实现:
    
    import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 定义邮箱的相关信息
sender = '2783523607@qq.com'
receiver = '483983530@qq.com'
pass_code = 'uqmypuziquxmdgdc'

# 链接邮箱服务
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)

# 邮件正文
content = '这是邮件的正文 这是邮件的正文 这是邮件的正文'
cont = MIMEText(content, 'plain', 'utf-8')

# 创建邮件对象
email = MIMEMultipart()
email.attach(cont)  # 添加正文

# 定义多个附件路径
attachments = [
    {'path': 'C:/Users/1/Pictures/111.jpg', 'filename': 'ROG.jpg'},
    {'path': 'C:/Users/1/Documents/file.pdf', 'filename': 'document.pdf'},
    {'path': 'C:/Users/1/Documents/data.xlsx', 'filename': 'data.xlsx'}
]

# 循环添加多个附件
for attachment_info in attachments:
    with open(attachment_info['path'], 'rb') as file:
        file_data = file.read()
    
    # 使用MIMEApplication处理二进制附件
    att = MIMEApplication(file_data)
    # 设置附件的Content-Disposition头信息
    att.add_header('Content-Disposition', 'attachment', 
                   filename=attachment_info['filename'])
    # 将附件添加到邮件中
    email.attach(att)

# 设置邮件基本信息
email['From'] = sender
email['To'] = receiver
email['Subject'] = Header('这个是带有多个附件的邮件', 'utf-8')

# 发送邮件
conn.login(sender, pass_code)
conn.sendmail(sender, receiver, email.as_string())

# 关闭连接
conn.close()


"""