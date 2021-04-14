'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-14 21:56:09
FilePath: \graduationProject\IM_analyze\test.py
'''
from flask import Flask
import pymysql


app = Flask(__name__)


@app.route('/')
def first_flask():
    print(1)
    return "hello word"


if __name__ == '__main__':
    app.run()
