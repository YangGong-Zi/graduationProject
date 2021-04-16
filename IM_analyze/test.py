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


def url_content_get(url):
    # 模拟是浏览器发出的请求,反爬
    # user_agent = 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    cookie = "cna=BzT3Fm6c7kUCAbfkzXgaAH0P; tracknick=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; enc=H2WcDBUg0yhhLLRDmdPoob0ooG0d41vbM2bFDNnVi1%2FP0e1gV9FATXDEA%2BZXlL0SB68MavPV8fM5kQ3CFeMw7w%3D%3D; miid=118309521405539638; _m_h5_tk=4ddfb77fd5812d4e385526cb4a242e33_1618591086537; _m_h5_tk_enc=14561b7542876dcc340e563fbec7ef6b; xlly_s=1; _samesite_flag_=true; cookie2=1699a0a764d5a1e935593620fedec3fc; t=faa474b2c81a3bcafc658c6e4b945dec; _tb_token_=33f9f71333606; sgcookie=E100PPspS5a6uQBqxXKP97cvVsJvmmbYI2Lz69PtsT%2FmIFNLgLlmbbmA05vaJYpNtgrOZwJwRxD%2FCTf9lnjwpWvChQ%3D%3D; unb=2747629526; uc3=nk2=VIFMlLqfPNcV&lg2=URm48syIIVrSKA%3D%3D&vt3=F8dCuwpnk9wWxA4VlAs%3D&id2=UU8M9askLNpfQw%3D%3D; csg=01233f58; lgc=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; cookie17=UU8M9askLNpfQw%3D%3D; dnk=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; skt=9f524a9a2a07b0dd; existShop=MTYxODU4MTM5OQ%3D%3D; uc4=nk4=0%40Vpj2qTie46tT97HwDpTbs2w6CIU%3D&id4=0%40U22LO6DaHwkRfbdwdqD15XWSSKFi; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%B8%856a; _nk_=7%5Cu73ED%5Cu7B2C%5Cu4E00%5Cu5E05; cookie1=BxAdfSrFIy3f2uC%2Fnlv10ccdW5LqlgvTQU0LbIflzsU%3D; mt=ci=25_1; uc1=cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=Uoe1iuWaMv1rxg%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&pas=0&existShop=false; hng=CN%7Czh-CN%7CCNY%7C156; isg=BA0NWuQtUZWsfMt_eQJm_j3tHCmH6kG863U080-SeaQTRiz4Fzt6jJvetNoghll0"
    ua = UserAgent()
    print(ua.random)
    headers = {
        'User-Agent': ua.random,
        'cookie': cookie
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status
        res.encoding = res.apparent_encoding
        # print(res.text)
        soup = BeautifulSoup(res.text, "html.parser")
        # print(soup.prettify)
        print(soup.findAll("dl"))
        return res.text
    except BaseException as e:
        print("getting text error!" + str(e))


def main():
    url = "https://huaweistore.tmall.com/i/asynSearch.htm?_ksTS=1618581772513_262&callback=jsonp263&mid=w-21620499162-0&wid=21620499162&path=/category-1350276998-1662001527.htm&spm=a1z10.1-b-s.w20163031-23245066575.2.27107597BhMgS9&search=y&parentCatId=1201482770&parentCatName=%CA%D6%BB%FA%D7%A8%C7%F8&parentCatPageId=1662001527&catName=Mate%CF%B5%C1%D0&scene=taobao_shop&catId=1350276998&scid=1350276998"
    url_content = url_content_get(url)
    # data = goods_message_to_file(url_content)
    # data_analysis_to_goods(data)


if __name__ == "__main__":
    main()
