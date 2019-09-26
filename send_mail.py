#!python3
#codin=utf-8
import yagmail
def send_mail():
    #缺失的qq用户和授权码
    yag = yagmail.SMTP(user='267798983@qq.com', password='inoxrruzdnjdjah', host='smtp.qq.com', port='465')
    body = "小程序接口测试之口算，请查收..."
    yag.send(to=['liuyanhui@xxx.com'], subject='小程序接口测试', contents=[body, './111.html'])
    print("已发送邮件")
send_mail()






# 1229159129@qq.com







