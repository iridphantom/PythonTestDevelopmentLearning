"""
    基于配置文件实现邮件的发送：
        smtp库默认是不支持给多人进行邮件发送。如果需要给多人发送邮件，则收件人一定要做数据的二次处理。
            也就是多人收件，收件人必须为list数据类型。不同的收件人邮箱地址为不同的元素。
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from class10_email.email_conf_demo import read

# 定义邮箱的相关信息
data = read('project')

print(data)    # {'sender': '2783523607@qq.com', 'receiver': '483983530@qq.com, nikola.yu.wang@outlook.com', 'pass_code': 'uqmypuziquxmdgdc'}

# receivers = ['2420574745@qq.com', '15414086@qq.com']    # 这是我们需要的格式，但实际获取的是一个str
# 对收件人格式进行二次定义
receivers = []
for receiver in data['receiver'].split(','):
    receivers.append(receiver)
print(receivers)    # ['483983530@qq.com', ' nikola.yu.wang@outlook.com']

# 链接邮箱服务
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)

# 邮件正文
content = '基于配置文件实现邮件的多人发送'
cont = MIMEText(content, 'plain', 'utf-8')

cont['From'] = data['sender']
cont['To'] = data['receiver']   # 只能是str，不能是list
cont['Subject'] = Header('这是发送邮件主题', 'utf-8')
# 发送邮件
conn.login(data['sender'], data['pass_code'])
conn.sendmail(data['sender'], receivers, cont.as_string())  # 真正意义上的邮件发送核心代码
conn.close()