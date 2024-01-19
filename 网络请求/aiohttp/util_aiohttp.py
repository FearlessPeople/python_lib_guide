# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_aiohttp.py.py
@create time: 2024/1/19 4:43 PM
@modify time: 2024/1/19 4:43 PM
@describe   : 
-------------------------------------------------
"""

import aiohttp

class AiohttpUtil:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get(self, url, params=None, headers=None, timeout=None):
        async with self.session.get(url, params=params, headers=headers, timeout=timeout) as response:
            return await response.text()

    async def post(self, url, data=None, json=None, headers=None, timeout=None):
        async with self.session.post(url, data=data, json=json, headers=headers, timeout=timeout) as response:
            return await response.text()

    def close_session(self):
        self.session.close()
