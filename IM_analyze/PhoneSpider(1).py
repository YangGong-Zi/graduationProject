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
#encoding:utf8

class PhoneSpider:
  """
      爬取天猫华为手机信息
      1.爬取字段:名称,价格,销量,评价
      2.只有一页数据,采取单线程,不考虑抓取效率
      3.数据结果以[{}, {}, {}, ..]形式存在
  """

  def __init__(self):
    self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36\
                        (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
    # self.login_url = 'https://login.tmall.com/' \
    #                  '?spm=a1z10.15-b-s.a2226mz.2.3a376a0clcjfzN&redirectURL=https%3A%2F%2Fhuaweistore.tmall.com' \
    #                  '%2Fcategory-1350276998-1662001527.htm%3FcatId%3D1350276998%26pageNo%3D1'
    # self.login_url = 'https://login.tmall.com/' \
    #                  '?spm=a1z10.15-b-s.a2226mz.2.3a376a0clcjfzN&redirectURL=https%3A%2F%2Fhuaweistore.tmall.com' \
    #                  '%2Fcategory-1350284311-1662001527.htm%3FcatId%3D1201482770%26pageNo%3D1'
    self.login_url = 'https://huaweistore.tmall.com/index.htm?spm=a1z10.5-b-s.w20163031-23245066575.17.3e301664w8WlSu'
    # 参数pageNo=1对应第几页数据
    # self.url = 'https://huaweistore.tmall.com/category-1350276998-1662001527.htm?catId=1350276998&pageNo=1'
  def getHuaweiUrl(self):
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
    time.sleep(10)
    response_text = driver.page_source
    response = etree.HTML(response_text)
    res = etree.tostring(response)
    # print(res)
    baseXpath = response.xpath('//*[@id="shop23245066575"]/div/div[2]/div/div/a/@href')
    print(baseXpath)
    # print("http://www.yunxiaojie.cn" + baseXpath[0])
    # for i in baseXpath:
    #   driver.get("http://www.yunxiaojie.cn" + i)
    #   res_1 = etree.HTML(driver.page_source)
    #   name = res_1.xpath('//span[@class="cor-orange"]/text()')
    #   print(name)
      # with open("name.txt", "w") as json_file:
      #   json_file.write(name[0])

  def parse_infos(self, user_name, password):
    """爬取手机信息"""
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
    # 填充点击登录
    driver.get(self.login_url)
    driver.switch_to.frame('J_loginIframe')
    # 用户名
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(user_name)
    # 密码
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
    # 点击登录
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    # 执行休眠10s等待浏览器的加载
    time.sleep(10)
    response_text = driver.page_source
    response = etree.HTML(response_text)
    # res = etree.tostring(response)
    # # print(res.decode('utf-8'))
    # baseXpath = response.xpath('//*[@id="shop23245066575"]/div/div[2]/div/div/a/@href')
    # print(baseXpath)
    # for i in baseXpath:
    #   print(i)

    for i in range(1, 3):
      base_xpath = response.xpath('//div[@class="J_TItems"]/div[@class="item4line1"][{}]/dl'.format(i))
      for dl in base_xpath:
        phone_name = dl.xpath('./dd[@class="detail"]/a/text()')[0]
        phone_price = dl.xpath('./dd/div/div[1]/span[2]/text()')[0].strip()
        # sale_num = dl.xpath('./dd/div/div[3]/span/text()')[0]
        sale_num = dl.xpath('./dd/div/div[3]/span/text()')
        # rates = dl.xpath('./dd/div/h4/a/span/text()')[0].split(':')[1].strip()
        rates = dl.xpath('./dd/div/h4/a/span/text()')
        phone_infos_dict = {
          'phone_name': phone_name,
          'phone_price': phone_price,
          'sale_num': sale_num,
          'rates': rates
        }
        phone_infos_list.append(phone_infos_dict)
    strjson = {"data": phone_infos_list}
    driver.close()
    # os.mknod("data.json")
    json_str = json.dumps(strjson, indent=4, ensure_ascii=False)
    with open("data.json", "w") as json_file:
      json_file.write(json_str)
    return phone_infos_list

  # def get_random_ip(self):
  #     """爬取代理ip"""
  #     privacy_ip = list()
  #     proxy_list = list()
  #     # 爬取前2页
  #     for i in range(1, 3):
  #         proxies_url = 'https://www.kuaidaili.com/free/inha/{}'.format(i)
  #         # 高匿IP
  #         response_text = requests.get(url=proxies_url, headers=self.headers).text
  #         response = etree.HTML(response_text)
  #         tr_xpath = response.xpath('//*[@id="list"]/table/tbody/tr')
  #         for td in tr_xpath:
  #             ip_address = td.xpath('./td[1]/text()')[0]
  #             ip_port = td.xpath('./td[2]/text()')[0]
  #             privacy_ip.append(ip_address + ':' + ip_port)
  #     # 检测代理ip可用性 to do
  #
  #     # 随机获取代理ip
  #     for ip in privacy_ip:
  #         proxy_list.append('http://' + ip)
  #     proxy_ip = random.choice(proxy_list)
  #     proxies = {'http': proxy_ip}
  #     return proxies
  #
  # def login(self):
  #     """模拟登录,保存cookies"""
  #     path = r'C:\Users\cyh\AppData\Local\Google\Chrome\Application\chromedriver'
  #     chrome_options = Options()
  #     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
  #     chrome_options.add_argument('--headless')
  #     chrome_options.add_argument('--disable-gpu')
  #     driver = webdriver.Chrome(executable_path=path, options=chrome_options)
  #     # 关闭开发者模式
  #     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  #         "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
  #     })
  #     # 填充点击登录
  #     driver.get(self.login_url)
  #     driver.switch_to.frame('J_loginIframe')
  #     # 用户名
  #     driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('15703031610')
  #     # 密码
  #     driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('cyh@1996')
  #     # 点击登录
  #     driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
  #     # 执行休眠3s等待浏览器的加载
  #     time.sleep(10)
  #     self.slid(driver)
  #     driver.close()
  #     # # 获取浏览器登陆后的cookies
  #     cookies = driver.get_cookies()
  #     # # 保存cookies，之后请求从文件中读取cookies就可以省去每次都要登录一次的，
  #     # # 通过json将cookies写入文件
  #     json_cookies = json.dumps(cookies)
  #     with open('Cookies.json', 'w') as f:
  #         f.write(json_cookies)
  #     print(cookies)
  #
  # def slid(self, driver):
  #     """滑动"""
  #     time.sleep(3)
  #     sliding = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')  # 滑动验证
  #     ActionChains(driver).drag_and_drop_by_offset(sliding, 170, 0).drag_and_drop_by_offset(sliding, 100,
  #                                                                                                0).perform()
  #     time.sleep(2)
  #     for i in range(3):
  #         refresh = driver.find_elements_by_xpath('//span[@class="nc-lang-cnt"]/a')
  #         if refresh:
  #             refresh[0].click()
  #             time.sleep(3)
  #             sliding = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')  # 滑动验证
  #             u = 200 + random.randint(0, 100)
  #             ActionChains(driver).drag_and_drop_by_offset(sliding, u, 0).perform()
  #             time.sleep(3)
  #         else:
  #             break
  #
  #     driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
  #     time.sleep(3)
  #
  # def parse_infos(self):
  #     """爬取手机信息"""
  #     if not Path('Cookies.json').exists():
  #         self.login()
  #     # 从文件中获取保存的cookies
  #     with open('Cookies.json', 'r', encoding='utf-8') as f:
  #         list_cookies = json.loads(f.read())  # 获取cookies
  #     # 把获取的cookies处理成dict类型
  #     cookies_dict = dict()
  #     for cookie in list_cookies:
  #         # 在保存成dict时，我们其实只要cookies中的name和value，而domain等其他都可以不要
  #         cookies_dict[cookie['name']] = cookie['value']
  #     print(cookies_dict)
  #
  #     phone_infos_list = list()
  #     proxies_ip = self.get_random_ip()
  #     response_text = requests.get(url=self.url, proxies=proxies_ip, cookies=cookies_dict, headers=self.headers)
  #     response = etree.HTML(response_text)
  #     for i in range(1, 3):
  #         base_xpath = response.xpath('//div[@class="J_TItems"]/div[@class="item4line1"][{}]/dl'.format(i))
  #         for dl in base_xpath:
  #             phone_name = dl.xpath('./dd[@class="detail"]/a/text()')[0].split('】')[1].strip()
  #             phone_price = dl.xpath('./dd/div/div[1]/span[2]/text()')[0].strip()
  #             sale_num = dl.xpath('./dd/div/div[3]/span/text()')[0]
  #             rates = dl.xpath('./dd/div/h4/a/span/text()')[0].split(':')[1].strip()
  #             phone_infos_dict = {
  #                 'phone_name': phone_name,
  #                 'phone_price': phone_price,
  #                 'sale_num': sale_num,
  #                 'rates': rates
  #             }
  #             phone_infos_list.append(phone_infos_dict)
  #     return phone_infos_list


if __name__ == '__main__':
  user_name = '15736392041'
  password = 'cf1210'
  phone_infos = PhoneSpider()
  # result = phone_infos.parse_infos(user_name, password)
  result = phone_infos.getHuaweiUrl()
  # print(result)

