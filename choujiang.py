#coding=utf-8
__author__ = "hui"
__date__ = "2019/5/16 16:51"

import csv,json,requests
day=0 # 當天還沒有抽獎
url="http://api.service.account.limiketang.com/award/draw"
if day==0:
    with open(r"C:\Users\26779\Desktop\5.9\new\award_test_token(4).csv", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            if line == 'token':
                continue

            r = requests.get(url=url, params={'token':line})
            print(r.content)
            #break






















