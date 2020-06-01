#!/usr/bin/env python
#conding:utf8

import requests
from lxml import etree
import re
from queue import Queue
from multiprocessing import pool
import time
p = re.compile('(\"https:.*?\")')
#获取下载id



def get_id(i):

    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
    url = "https://www.ximalaya.com/youshengshu/12296837/p%d/"%i
    print(url)
    response = requests.get(url,headers=header)
    html = etree.HTML(response.text)
    id_list = html.xpath('//div[@class="text _Vc"]/a/@href')
    id_list = [id_list[i][-8:] for i in range(len(id_list))]
    print("--------------")
    print(id_list)
    get_url(id_list)

queue = Queue()
#获取下载链接
def get_url(id):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    for i in range(len(id)):
        url = "https://www.ximalaya.com/revision/play/v1/audio?id=%8d&ptype=1"%(int(id[i]))
        print("+++++++++++++++")
        print(url)
        #time.sleep(0.01)
        response = requests.get(url,headers=headers)
        print(response.status_code)
        print(response.text)

        print("huoqudessssssssssssssss")
        print(response.text)
        m4a_url = p.search(response.text).group(0)
        print("#######################")
        print(m4a_url)
        #print("=============")
        #print(m4a_data)
        queue.put(m4a_url)

#下载
def down_m4a(url):
    #url = queue.get()
    print("从队列中获取数据")
    print(url)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    response = requests.get(url,headers=header)
    print('00000000000000000000')
    print(response.status_code)
    with open(url[-9:],"wb") as f:
        f.write(response.content)

def down_pool():
    dp = pool.Pool(4)
    while(queue.qsize()>=0):
        dp.apply_async(down_m4a,args=(queue.get(),))
    dp.close()
    dp.join()


def main():
    p = pool.Pool(4)
    for i in range(1,2):
        p.apply_async(get_id(i),args=(i,))

    p.close()
    p.join()

if __name__ == '__main__':
    main()

    down_pool()
    print(queue.qsize())
    if queue.empty():
        print("链接获取完毕")



