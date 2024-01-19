# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_httpx.py
@create time: 2024/1/19 5:00 PM
@modify time: 2024/1/19 5:00 PM
@describe   : 
-------------------------------------------------
"""
# util_httpx.py

import httpx

class HttpxUtil:
    def __init__(self):
        self.client = httpx.Client()

    def get(self, url, params=None, headers=None):
        response = self.client.get(url, params=params, headers=headers)
        return response.text

    def post(self, url, data=None, json=None, headers=None):
        response = self.client.post(url, data=data, json=json, headers=headers)
        return response.text

    def close_client(self):
        self.client.close()


