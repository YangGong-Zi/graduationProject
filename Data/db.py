'''
Author: 在下杨公子
Date: 2021-04-14 23:06:26
LastEditTime: 2021-04-15 00:46:00
FilePath: \graduationProject\IM_analyze\db.py
'''
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', db='forum',
                       passwd='root', charset='utf8', autocommit=True)
cur = conn.cursor()
try:
    create_sqli = "show tables;"
    cur.execute(create_sqli)
    res = cur.fetchall()
    print(res)
except Exception as e:
    print("failed:", e)
else:
    print("success")
cur.close()
conn.close()
