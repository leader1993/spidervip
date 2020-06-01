#!/usr/bin/env python
#conding:utf8
"""
通过js网站来获取片段信息
爬取片段信息
合并片段 copy /b *.ts 文件名
"""
'''
https://wqxuetang.oss-cn-beijing.aliyuncs.com/cover/3/203/3203922/3203922.jpg!wqb
https://youku.cdn7-okzy.com/20191203/16033_b28cd947/1000k/hls/0d2d28c500600%04d.ts

https://youku.cdn7-okzy.com/20200324/18160_936263ee/1000k/hls/54040aae408000001.ts
https://youku.cdn7-okzy.com/20200324/18160_936263ee/1000k/hls/54040aae408001631.ts
'''
import requests
from multiprocessing import Pool

def down_aiqiyi(i):
    url = "https://youku.cdn7-okzy.com/20200324/18160_936263ee/1000k/hls/54040aae40800%04d.ts"% i
    print(url)
    response = requests.get(url)

    res_tv = response.content

    with open("./dianying/{}".format(url[-10:]),"wb") as f:
        f.write(res_tv)


if __name__ == '__main__':
    pool = Pool(20)
    for i in range(1522,1632):
        pool.apply_async(down_aiqiyi,args=(i,))

    pool.close()
    pool.join()