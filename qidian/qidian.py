#!/usr/bin/env python
#conding:utf8

from fontTools.ttLib import TTFont
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}

url = "https://book.qidian.com/info/1017514184"
response = requests.get(url,headers=headers)
html_page = response.text
print(html_page)
print(response.status_code)

#转换字体文件
font = TTFont("qidian.woff")
font.saveXML("qidian.xml")

dict = font["cmap"].getBestCmap()
dict_a = {100261: 'eight', 100263: 'one', 100264: 'six', 100265: 'seven', 100266: 'period', 100267: 'three', 100268: 'nine', 100269: 'four', 100270: 'two', 100271: 'zero', 100272: 'five'}
dict_b = {'eight':"8", 'one':"1", 'six':"6", 'seven':'7', 'period':'.', 'three':'3', 'nine':'9', 'four':'4', 'two':'2', 'zero':'0', 'five':'5'}

for key in dict_a:
    dict_a[key] = dict_b[dict_a[key]]

print(dict_a)

for k in dict_a:
    if str(k) in html_page:
        print(k)
        html_page = html_page.replace("&#"+str(k)+";",dict_a[str(k)])
print(html_page)



#print(dict_b)
#print(dict)

