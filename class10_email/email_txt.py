"""
    文本邮件的发送：
        发送纯文本的邮件信息，不包含任何其他内容在内，
    属于邮件中最基本的一种发送形态
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 定义邮箱的相关信息
sender = '2783523607@qq.com'
receiver = '483983530@qq.com'
pass_code = 'uqmypuziquxmdgdc'

# 链接邮箱服务
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 这是QQ邮箱的smtp服务器地址与端口号, SSL方式发送.25（不使用SSL） 465（使用SSL） 587（使用SSL）

# 邮件正文
content = '''
    SMTP邮件发送：
    这是一份txt文件，通过smtplib库实现。
'''

# 将正文写入邮件之中
cont = MIMEText(content, 'plain', 'utf-8')  # plain表示纯文本邮件


# 将邮件的发件人与收件人进行定义
cont['From'] = sender  # 定义发件人
cont['To'] = receiver  # 定义收件人
cont['Subject'] = Header('这个是邮件的主题——txt文件', 'utf-8')  # 设置邮件的主题

# 发送邮件
conn.login(sender, pass_code)  # 基于发件人账号与授权码进行smtp服务的登录
conn.sendmail(sender, receiver, cont.as_string())  # 将定义好的邮件进行发送

# 邮箱服务关闭
conn.close()