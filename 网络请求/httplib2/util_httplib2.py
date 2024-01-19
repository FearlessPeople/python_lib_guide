# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_httplib2.py.py
@create time: 2024/1/19 5:19 PM
@modify time: 2024/1/19 5:19 PM
@describe   : 
-------------------------------------------------
"""

import httplib2
import urllib.parse

class Httplib2Util:
    def __init__(self):
        self.http = httplib2.Http()

    def get(self, url):
        response, content = self.http.request(url, 'GET')
        return content

    def post(self, url, data):
        body = urllib.parse.urlencode(data)
        response, content = self.http.request(url, 'POST', body=body)
        return content

