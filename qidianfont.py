#!/usr/bin/env python
#conding:utf8
'''
from fontTools.ttlib import TTFont
font_file = TTFont("")
font_file.saveXML("")
font_dict = font_file["cmp"].getBextMap()


'''

import requests
import re
from fontTools.ttLib import TTFont
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}

url = "https://book.qidian.com/info/1017514184"
response = requests.get(url,headers=headers)

print(response.status_code)

#获取字体文件链接并且将字体下载下来
font_url = re.findall("; src: url\('(.*?')\) format",response.text)[0]
print(font_url)
#下载字体
font_response = requests.get(font_url,headers=headers)
with open("font_1.woff","wb") as f:
    f.write(font_response.content)
#字体文件可视化
fi = TTFont("font_1.woff")
fi.saveXML("font.xml")

#获取加密文件
sec_dict = fi["cmp"].getBextMap()
#创建解密字典
d = {"sec_dict【k】":"实际数字"}
#对加密数字进行替换,获取解密后的字典
for key in sec_dict:
    sec_dict[key]=d[sec_dict[key]]

#对爬去页面的加密数据进行替换
for key in sec_dict:
    html = response.text.replace("key",sec_dict[key])

#对解密后的数据进行处理
html.xpath()



with open("起点小说.html","w",encoding="utf8") as f:
    f.write(response.text)

