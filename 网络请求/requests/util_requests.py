# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_requests.py
@create time: 2024/1/19 4:36 PM
@modify time: 2024/1/19 4:36 PM
@describe   : 
-------------------------------------------------
"""
import requests

class RequestsUtil:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, headers=None, timeout=None):
        response = self.session.get(url, params=params, headers=headers, timeout=timeout)
        return response

    def post(self, url, data=None, json=None, headers=None, timeout=None):
        response = self.session.post(url, data=data, json=json, headers=headers, timeout=timeout)
        return response

    def close_session(self):
        self.session.close()
