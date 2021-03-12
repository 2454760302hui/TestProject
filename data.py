# coding=utf-8
from faker import Faker
from custom.custom import MyProvider
import pandas as pd
import pymysql
class Create_Data(object):
    def __init__(self):

        # 选择中文
        fake = Faker('zh_CN')

        #生成的字段内容
        self.data_total = [
            ['this is test', fake.job(), fake.company(), fake.phone_number(), fake.company_email(),
             '受理中','早班客服组','早班客服1', fake.date_time()] for x in range(10000)]
        print(self.data_total)
    def deal_excel(self):

        #生成的表格字段
        df = pd.DataFrame(self.data_total,
                          columns=['工单标题（必填）', '工单描述（必填)', '客户昵称', '客户手机', '客户邮箱', '状态(必填)', '创建时间','受理客服组','受理客服'])
        # 保存到本地excel
        df.to_excel(r"C:\Users\Administrator\Desktop\data.xlsx", index=False)
        print("done")

if __name__=="__main__":
    data = Create_Data()

    data.deal_excel()
