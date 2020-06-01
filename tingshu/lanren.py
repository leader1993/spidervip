#!/usr/bin/env python
#conding:utf8

'''

http://wting.info/asdb/fiction/xuanhuan/zzds/8guv411c.mp3
http://wting.info/asdb/fiction/xuanhuan/zzds/w0ett5jy.mp3
http://www.lrts.me/ajax/playlist/2/30025/3
'''
import requests
from lxml import etree

url = "http://www.lrts.me/ajax/playlist/2/30025/1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

res = requests.get(url,headers=header)
print(res.text)
print(res.encoding)

html = etree.HTML(res.text)
url_list = html.xpath('//input[@name="source"]/@value')
print(url_list)