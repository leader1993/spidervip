#!/usr/bin/env python
#conding:utf8

import requests

res = requests.get("http://www.baidu.com")
print(res.status_code)
