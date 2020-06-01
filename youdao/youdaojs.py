#!/usr/bin/env python
#conding:utf8

import requests

import hashlib
from datetime import datetime
import time
e = "hello"
salt = "15827198227411"
sign = "db724da409d815e778787828fae9f812"
ts= "1582719822741"
bv = "d6c3cd962e29b66abe48fcb8f4dd7f7d"
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {
    'i':e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

}

response = requests.post(url,headers=headers,data=data)
print(response.text)
