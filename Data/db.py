'''
Author: 在下杨公子
Date: 2021-04-14 23:06:26
LastEditTime: 2021-04-15 00:46:00
FilePath: \graduationProject\IM_analyze\db.py
'''
import pymysql
import json

with open("..\\static\\data\\data.json", 'r', encoding='utf-8') as f: #打开json文件
  list = json.load(f)
conn = pymysql.connect(host='localhost', user='root', db='data',
                       passwd='root', charset='utf8', autocommit=True) #配置数据库链接参数
cur = conn.cursor() #定义游标
try:
  for i in list:
    for j in range(len(list[i]["time"])):
      create_sqli = "insert into phone (phone_brand,phone_name,phone_price,phone_sales) values (%s,%s,%s,%s)" #数据库语句
      cur.execute(create_sqli,(i,list[i]["time"][j],list[i]["price"][j],list[i]["number"][j])) #执行数据库语句
except Exception as e:
  print("failed:", e)
else:
  print("success")
cur.close() #关闭游标
conn.close() #关闭数据库链接
