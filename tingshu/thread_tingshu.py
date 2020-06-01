#!/usr/bin/env python
#conding:utf8

import requests
from lxml import etree
import re
from queue import Queue
from multiprocessing import pool
from threading import Thread,Lock
import time
p = re.compile('(\"https:.*?\")')
#获取下载id
#多线程爬取听书

lock = Lock()
lock_b = Lock()
def response_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    return response

def get_id(i):
    url = "https://www.ximalaya.com/youshengshu/12296837/p%d/"%i
    print(url)
    response = response_html(url)
    html = etree.HTML(response.text)
    id_list = html.xpath('//div[@class="text _Vc"]/a/@href')
    id_list = [id_list[i][-8:] for i in range(len(id_list))]
    print("--------------")
    print(id_list)
    get_url(id_list)

queue = Queue()
#获取下载链接
def get_url(id):
    for i in range(len(id)):
        url = "https://www.ximalaya.com/revision/play/v1/audio?id=%8d&ptype=1"%(int(id[i]))
        print(url)
        #time.sleep(0.01)
        response = response_html(url)
        print(response.status_code)
        print(response.text)
        m4a_url = p.search(response.text).group(0)
        print("#######################")
        print(m4a_url)
        #print("=============")
        #print(m4a_data)
        lock.acquire()
        queue.put(m4a_url)
        lock.release()

#下载
def down_m4a():
    while(queue.qsize()>=0):
        url = queue.get()
        print("从队列中获取数据")
        print(url[1:-1])
        url = url[1:-1]
        response =response_html(url)
        print('00000000000000000000')
        with open(url[-9:],"wb") as f:
            f.write(response.content)

def down_pool():

    t3 = Thread(target=down_m4a)
    t3.start()
    t3.join()

def get_id_url(i,j):
    for a in range(i,j):
        get_id(a)

def main():
    t1 = Thread(target=get_id_url,args=(1,4,))
    t1.start()
    t1.join()
    t2 = Thread(target=get_id_url, args=(4,9))
    t2.start()
    t2.join()



if __name__ == '__main__':
    main()
    down_pool()
    print(queue.qsize())
    if queue.empty():
        print("链接获取完毕")



