#!/usr/bin/env python
#conding:utf8
import random

import requests

import hashlib
from datetime import datetime
import time


def get_md5(name):
    name = name.encode("utf-8")
    md5 = hashlib.md5(name).hexdigest()
    return md5


#print(get_md5("莫海军"))
'''
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
            eb9c1268a950e6eddb2708071f6b0d52

'''
e ="华为"
r = str(time.time()*1000)[0:13]
salt = r + str(random.randint(0,9))
bv = get_md5("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
sign = get_md5("fanyideskweb" + e + salt + "Nw(nmmbP%A-r6U3EUn]Aj")
# time = datetime.now()
# ts = str(time.timestamp())
# salt = ts +
print(r)
print(salt)
print(bv)
print(sign)

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {
    'i':e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': r,
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