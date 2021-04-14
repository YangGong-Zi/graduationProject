'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-12 22:05:30
FilePath: \graduationProject\IM_analyze\test.py
'''
from flask import Flask
import pymysql


app = Flask(__name__)
@app.route('/')
def first_flask():
    print(1)
    return "hello word"

@app.route('/caonima')
def caonima():
    return "hello word"

first_flask();

if __name__=='__main__':
    app.run()   