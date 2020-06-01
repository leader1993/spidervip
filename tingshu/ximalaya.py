#!/usr/bin/env python
#conding:utf8

import requests

"""
https://www.ximalaya.com/revision/play/v1/audio?id=252758768&ptype=1
https://www.ximalaya.com/revision/play/v1/audio?id=64591880&ptype=1
https://www.ximalaya.com/revision/play/v1/audio?id=64591881&ptype=1
https://fdfs.xmcdn.com/group63/M07/FE/E7/wKgMaF0mqm7gg8VOAGi_HOQrJNw535.m4a
"""
'''
正则表达式
(\"src\"\:\".+\",)："src":"https://fdfs.xmcdn.com/group63/M07/FE/E7/wKgMaF0mqm7gg8VOAGi_HOQrJNw535.m4a",
(\"https:.*?\")："https://fdfs.xmcdn.com/group63/M07/FE/E7/wKgMaF0mqm7gg8VOAGi_HOQrJNw535.m4a"
#
'''
# 获取id值
'''
页数：https://www.ximalaya.com/youshengshu/12296837/p29/
列表：
 处理列表方法b = [b[i][-9:]for i in range(len(b))]
'''
from lxml import etree
url = "https://www.ximalaya.com/revision/play/v1/audio?id=64861950&ptype=1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

response = requests.get(url,headers=headers)
print(response.status_code)
html = response.text
print(html)
#html_xpath = etree.HTML(html)
# htmlid_list = html_xpath.xpath('//div[@class="text _Vc"]/a/@href')
# print(id_list)
#print(response.text)
#print(response.json())

# with open(url[-8:],"wb")as f:
#     f.write(response.condingtent)