#!/usr/bin/env python
#conding:utf8

import requests
import pprint
import json

#url = "http://www.kuwo.cn/play_detail/26413118"
#url = "http://www.kuwo.cn/url?format=mp3&rid=7149583&response=url&type=convert_url3&br=128kmp3&from=web&t=1582207510791&reqId=01ec2f90-53ea-11ea-8d80-d746bc6583b0"
url = "http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery1720323037982024867_1582210375236&songid=1332939&from=web&_=1582210378073"
response = requests.get(url)
#result = json.loads(response.content)

#musdic_url = musdic_dict["url"]
#m_response = requests.get(musdic_url)

#with open("1111.mp3","wb") as f:
#    f.write(m_response.content)
pprint.pprint(response.text)
