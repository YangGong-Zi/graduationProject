'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-17 00:05:23
FilePath: \graduationProject\IM_analyze\test.py
'''
from flask import Flask
import pymysql
import re
from bs4 import BeautifulSoup
import requests
import json
# import pygal
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import pickle
import os

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def getTaobaoCookies():
  url = "https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.5af911d91fT2Y1&nekot=N7DgtdrSu8un1618649518100"
  driver.get("https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.5af911d91fT2Y1&nekot=N7DgtdrSu8un1618649518100")
  while True:
    time.sleep(3)
    while driver.current_url == url:
      # tbCookies = driver.get_cookies()
      # driver.quit()
      # cookies = {}
      # for item in tbCookies:
      #   cookies[item['name']] = item['value']
      # outputPath = open('taobaoCookies.pickle', 'wb')
      # pickle.dump(cookies, outputPath)
      # outputPath.close()
      return cookies

def readTaobaoCookies():
    readPath = open('taobaoCookies.pickle', 'rb')
  if os.path.exists('taobaoCookies.pickle'):
    tbCookies = pickle.load(readPath)
  else:
    tbCookies = getTaobaoCookies()
  return tbCookies



def url_content_get(url):
  # 模拟是浏览器发出的请求,反爬
  # user_agent = 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
  cookie = "hng=CN%7Czh-CN%7CCNY%7C156; lid=7%E7%8F%AD%E7%AC%AC%E4%B8%80%E5%B8%85; cna=xJbgGKUxqCoCAX1S8snnBwY9; xlly_s=1; pnm_cku822=; dnk=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; uc1=cookie14=Uoe1iua7K1%2ByuA%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0&existShop=false; uc3=id2=UU8M9askLNpfQw%3D%3D&nk2=VIFMlLqfPNcV&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dCuwpkh2c88isQKMQ%3D; tracknick=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; uc4=nk4=0%40Vpj2qTie46tT97HwDpTYbHRJJG0%3D&id4=0%40U22LO6DaHwkRfbdwdqD15sRu%2Fc8R; _l_g_=Ug%3D%3D; unb=2747629526; lgc=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; cookie1=BxAdfSrFIy3f2uC%2Fnlv10ccdW5LqlgvTQU0LbIflzsU%3D; login=true; cookie17=UU8M9askLNpfQw%3D%3D; cookie2=2833226ae3bd1937f099fe4a71b4e25c; _nk_=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; sgcookie=E100irLp1rYVQqFrO%2Brl1gQe09oPX59t8euM%2BzAkq0V7r7hcC4xzVdFwM%2BaEbmQZJeZk1ggN63py0QQp0oeYXqAdpg%3D%3D; t=b095cd020c5d6569a2b4ccbe3df62cd1; sg=%E5%B8%856a; csg=1853720d; enc=wzeKHZYKQrGm3xv8iMASiZRkOJDKM38dYzk4Epx4SXTRZKlrndJEHV6h2b%2BGnYU%2F%2FrJQ8YbAu%2FA5F9nL8qyvdA%3D%3D; _tb_token_=773116bbbede3; tfstk=c86RBwaGWr4kwT-Ab_FmAOVGvsrcwyapl0TnpuFQlagpRE1DvOXOsOFWA4pYD; l=eBP_AqorjwHFIXfABOfZourza779jIRAguPzaNbMiOCPOzfp5ff1W6aZWoY9CnGVh6-pR3leHMv_BeYBqI2RLBETjk5zgSMmn; isg=BL6-x43wUhMG3YY0pBp021bdD9QA_4J5Zx2662jHL4H8C17l0I7oi8vtg9fHM3qR"
  ua = UserAgent()
  print(ua.random)
  headers = {
    # ":authority": "huaweistore.tmall.com",
    # ":method": "GET",
    'User-Agent': ua.random,
    'cookie': cookie,

  }
  try:
    res = requests.get(url, headers=headers)
    res.raise_for_status
    res.encoding = res.apparent_encoding
    # print(res.text)
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.prettify)
    # print(soup.findAll("dl"))
    # print(soup.findAll("a"))
    print(soup.findAll("dl", class_="item"))
    return res.text
  except BaseException as e:
    print("getting text error!" + str(e))


def main():
  url = "https://detail.tmall.com/item.htm?spm=a1z10.15-b-s.w4011-21620499162.65.71b16a0cZscs74&id=630289014447&rn=5f8362bcfdb77300da0024893aca499e&abbucket=12"
  url_content = url_content_get(url)
  # data = goods_message_to_file(url_content)
  # data_analysis_to_goods(data)

if __name__ == "__main__":
  # tbCookies = readTaobaoCookies()
  options.add_argument("C:\\Users\\EDZ\\AppData\\Local\\Google\\Chrome\\User Data")
  options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
  driver.maximize_window()
  driver.get('https://www.taobao.com/')
  print(driver.get_cookies())
