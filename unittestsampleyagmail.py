#!coding=utf-8
#python3
import unittest,HTMLTestRunner
from test_case import send_mail
# print(help(unittest))
class Test(unittest.TestCase):
    def test_add(self):
        a=1
        b=2
        c=a+b
        self.assertEquals(c,3)

if __name__=="__main__":
    suite = unittest.TestSuite()  # 定义一个测试集合
    suite.addTest(unittest.makeSuite(Test))  # 把写的用例加进来（limi_kousuan）加进来
    f = open('./111.html', 'wb')  # 以二进制模式打开一个文件 ,u'C:\\Users\\26779\\Desktop\\小程序.html'
    runner = HTMLTestRunner.HTMLTestRunner(f, title='unittest用例标题', description='这是用例描述')
    runner.run(suite)  # 运行用例（用例集合)



