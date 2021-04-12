'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-12 22:05:30
FilePath: \graduationProject\IM_analyze\test.py
'''
# print('中文');
from bs4 import BeautifulSoup
import requests
def getdata():
    res = requests.get(url,headers = "mingker.cn")
    soup = BeautifulSoup(res.content,'lxml')
    return soup
def main():
    getdata()
if __name__ == '__main__':
    main()