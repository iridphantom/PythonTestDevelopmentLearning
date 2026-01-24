"""
    网页邮件的发送：
        发送一封内容为html的邮件。
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 定义邮箱的相关信息
sender = '2783523607@qq.com'
receiver = '483983530@qq.com'
pass_code = 'uqmypuziquxmdgdc'
# 链接邮箱服务
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)

# 邮件正文
content = '''
    <p> 这是一封HTML邮件 </p>
    <a href="https://www.baidu.com">点我访问百度</a>
'''
cont = MIMEText(content, 'html', 'utf-8')

# 将邮件的发件人与收件人进行定义
cont['From'] = sender  # 定义发件人
cont['To'] = receiver  # 定义收件人
cont['Subject'] = Header('这个是邮件的主题——HTML邮件', 'utf-8')  # 设置邮件的主题

# 发送邮件
conn.login(sender, pass_code)  # 基于发件人账号与授权码进行smtp服务的登录
conn.sendmail(sender, receiver, cont.as_string())  # 将定义好的邮件进行发送

# 邮箱服务关闭
conn.close()