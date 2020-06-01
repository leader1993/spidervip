#!/usr/bin/env python
#conding:utf8
import requests
import pprint


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",

}

url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1417862065?csrf_token="
"https://music.163.com/weapi/v1/resource/comments/R_SO_4_1422992414?csrf_token="
datas = {
"params": "FFRDUasEdMj4Vct+Pv0xMtrWNvtZcjesOcUON2iWIi+cTsjc9VGALvytmyf/9UpRhB9KsX1VhzVkDuu+upgHOkMcHSdGcHh8PXPx0lG/Ay0tz+SbOOA0cL3eRCkLHsBHZ6bX/Fxmq7U4VeQz+ILMw4roAWjLPNYAKR/1yv60wkGkASzg+YIPociL5oz+DB3p",
"encSecKey": "2b9c98e7d88b19fe2465e6c3830278ade3c429fd505c033684c6da56fe7822fbc9bd60f82a21806e5ebf34790b3b4e6b7af7ec1ca740800d85149c98ac4c71035cc07f86f22e93dcae19fbb01977a98cdf4922ea870752fe32989835e6e6e315c8d66d9e1fd2995059ea813487df07e2ae6a089e1b4200b7648c617ec296f9f6"
}
response = requests.post(url,data=datas,headers=headers)
pprint.pprint(response.json())
'''

!function () {
#随机的字符串
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) e = Math.random() * b.length, e = Math.floor(e), c += b.charAt(e);
        return c
    }

    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b), d = CryptoJS.enc.Utf8.parse("0102030405060708"),
            e = CryptoJS.enc.Utf8.parse(a), f = CryptoJS.AES.encrypt(e, c, {iv: d, mode: CryptoJS.mode.CBC});
        return f.toString()
    }

    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131), d = new RSAKeyPair(b, "", c), e = encryptedString(d, a)
    }

params：需要第一个参数和第四个参数
enc：需要第二个参数和第三个参数和一个i
    function d(d, e, f, g) {
        var h = {}, i = a(16);
        return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
    }

    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d), f
    }

    window.asrsea = d, window.ecnonasr = e

@font-face { font-family: gbvrVCrW; src: url('?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/gbvrVCrW.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/gbvrVCrW.ttf') format('truetype'); } .gbvrVCrW { font-family: 'gbvrVCrW' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }
'''