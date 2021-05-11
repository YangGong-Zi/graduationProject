# -*- coding: utf-8 -*-
import requests
import time
import random
import json
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from pathlib import Path
from lxml import etree
from collections import defaultdict, OrderedDict


def getHuaweiUrl():
  phone_infos_list = list()
  # 设置谷歌无界面浏览器
  path = r'C:\Users\EDZ\AppData\Local\Programs\Python\Python39\Scripts\chromedriver'
  # path = r'C:\Users\Cistella\AppData\Local\Programs\Python\Python39\Scripts\chromedriver'
  chrome_options = Options()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  driver = webdriver.Chrome(executable_path=path, options=chrome_options)
  # 关闭开发者模式
  driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
  })
  url = "https://huaweistore.tmall.com/index.htm?spm=a1z10.1-b-s.w20163031-23245066575.17.4e977597KlH6Ca"
  driver.get(url)
  # time.sleep(10)
  response_text = driver.page_source
  response = etree.HTML(response_text)
  # res = etree.tostring(response)
  # print(res)
  baseXpath = response.xpath('//*[@id="shop23245066575"]/div/div[2]/div/div/a/@href')
  for i in baseXpath:
    print( "https:" + i)
  driver.get("https:" + baseXpath[1])
  res_text = driver.page_source
  res = etree.HTML(res_text)
  # print(etree.tostring(res))
  text = res .xpath('//*[@id="J_ShopSearchResult"]/div/div[3]/div[1]')
  print(text)
  # print("http://www.yunxiaojie.cn" + baseXpath[0])
  # for i in baseXpath:
  #   driver.get("http://www.yunxiaojie.cn" + i)
  #   res_1 = etree.HTML(driver.page_source)
  #   name = res_1.xpath('//span[@class="cor-orange"]/text()')
  #   print(name)
  # with open("name.txt", "w") as json_file:
  #   json_file.write(name[0])
if __name__ == '__main__':
    getHuaweiUrl()
