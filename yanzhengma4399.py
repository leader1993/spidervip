#!/usr/bin/env python
#conding:utf8
'''

使用xpth，减轻查找时间
'''
from selenium import webdriver
from PIL import  Image

dirver = webdriver.PhantomJS(executable_path=r'C:/soft/phantomjss/phantomjs-2.1.1-windows/bin/phantomjs.exe')
dirver.set_window_size(1920, 1080)
dirver.get("http://www.4399.com")
#点击登录
dirver.find_element_by_xpath('//*[@id="login_tologin"]').click()
#dirver.switch_to.frame("popup_login_frame")
element = dirver.find_element_by_id("popup_login_frame")
#element.screenshot("login_1.png")
#跳转到frame框架
#dirver.switch_to.frame("popup_login_frame")
#dirver.find_element_by_xpath('//*[@id="username"]').send_keys("15637043508")
#dirver.find_element_by_xpath('//*[@id="j-password"]').send_keys("mhj123123")
#dirver.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[5]/input').click()

#保存截图
#dirver.save_screenshot("4399_login_2.png")
#获取登录框架的位置
print(element.location)
print(element.size)
#进行截取
im = Image.open("login_1.png")
left = element.location["x"]
top = element.location["y"]
hheight = top+element.size["height"]
wwidth = left + element.size[ 'width']
im = im.crop((left,top,wwidth,hheight))
im.save("b.png")


