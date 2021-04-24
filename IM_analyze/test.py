'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-17 00:05:23
FilePath: \graduationProject\IM_analyze\test.py
'''
from flask import Flask
import pymysql
import re
import json

app = Flask(__name__)  # 创建1个Flask实例


@app.route('/')  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():  # 视图函数
  # with open("data.json", 'r', encoding='UTF-8') as f:
  #   load_dict = json.load(f)
  return "load_dict "  # response


@app.route('/getData',methods=["POST"] )  # 路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def getData():  # 视图函数
  with open("data.json", 'r') as f:
    # print(type(f))
    load_dict = json.load(f)
    print(load_dict)
    # res = json.dumps(f)
  return load_dict


if __name__ == '__main__':
  app.run()
