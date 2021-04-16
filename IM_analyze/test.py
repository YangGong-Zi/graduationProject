'''
Author: 在下杨公子
Date: 2021-04-12 21:09:21
LastEditTime: 2021-04-14 21:56:09
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



def url_content_get(url):

    # 模拟是浏览器发出的请求,反爬
    # user_agent = 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    cookie = "dnk=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie14=Uoe1iuWXIxk%2Fkw%3D%3D; uc3=id2=UU8M9askLNpfQw%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dCuwpnkAHfXlRnySE%3D&nk2=VIFMlLqfPNcV; tracknick=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; lid=7%E7%8F%AD%E7%AC%AC%E4%B8%80%E5%B8%85; uc4=nk4=0%40Vpj2qTie46tT97HwDpTbvnuFaf8%3D&id4=0%40U22LO6DaHwkRfbdwdqD15XhKLHSz; _l_g_=Ug%3D%3D; unb=2747629526; lgc=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; cookie1=BxAdfSrFIy3f2uC%2Fnlv10ccdW5LqlgvTQU0LbIflzsU%3D; login=true; cookie17=UU8M9askLNpfQw%3D%3D; cookie2=15c022a3b083451ea5b137615ef6d7ad; _nk_=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; sgcookie=E100rWz6MRqdNkQ5FZyYzGyfD5xlgCxnrgjxJYw%2F43IU4yLyGxTu6q0uaFpjZ9M5kPifvpnFLpxL%2BoTTWC%2BJNxisEA%3D%3D; t=4456a715b126a8bed6423e7810e5928f; sg=%E5%B8%856a; csg=72491d13; enc=i%2F23GDbrgXw8ZKGS2moyMpYcDoEGalI95mzUovDYzxg7Vd3F3YLk5OHZClJQL9Y5%2BCXE4L4Iqcxki92NwWLcqw%3D%3D; _tb_token_=f705a751bbe7; cna=xJbgGKUxqCoCAX1S8snnBwY9; xlly_s=1; pnm_cku822=; x5sec=7b2273686f7073797374656d3b32223a223937396561663266313361623534613939623739306135613132616232663563434a367135594d474549477938666a70792b793636414561444449334e4463324d6a6b314d6a59374d5367434d4f5868743737352f2f2f2f2f77453d227d; tfstk=cMrPBmmOmgIyR3oCW0ieOKHfjcnRw2wuKnksrrferDxU9YfcTBHcEPDqdfImr; l=eBP_AqorjwHFIf8jKOfanurza77OSIRYYuPzaNbMiOCPOv1B5BTFW6asveT6C3GVh6SpR3leHMv6BeYBq3xonxvTjk5zgSkmn; isg=BN_f4O4gw-9ouMfzXXFFFL-WbjNpRDPmPka7bHEseA7VAP-CeRWCN2zWwpB-mAte"
    ua = UserAgent()
    print(ua.random)
    headers = {
            'User-Agent': ua.random,
            'cookie':cookie
        }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status
        res.encoding = res.apparent_encoding
        # print(res.text)
        soup= BeautifulSoup(res.text,"html.parser")
        # print(soup.prettify)
        print(soup.findAll("dl"))
        return res.text
    except BaseException as e:
        print("getting text error!"+str(e))



def main():
    url = "https://huaweistore.tmall.com/i/asynSearch.htm?_ksTS=1618564464878_264&callback=jsonp265&mid=w-21620499162-0&wid=21620499162&path=/category-1350276998-1662001527.htm&spm=a1z10.1-b-s.w20163031-23245066575.2.71007597yOCj0D&search=y&parentCatId=1201482770&parentCatName=%CA%D6%BB%FA%D7%A8%C7%F8&parentCatPageId=1662001527&catName=Mate%CF%B5%C1%D0&scene=taobao_shop&catId=1350276998&scid=1350276998"
    url_content = url_content_get(url)
    # data = goods_message_to_file(url_content)
    # data_analysis_to_goods(data)


if __name__ == "__main__":
    main()
