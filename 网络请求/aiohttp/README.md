# aiohttp

## 简介

[aiohttp](https://github.com/aio-libs/aiohttp) 是一个用于发送异步HTTP请求的Python库，基于Python的 `asyncio`
模块。它支持异步请求和响应操作，适用于构建异步的Web应用和服务。

**特性**

- **异步请求:** 提供异步请求支持，适用于同一线程中处理多个请求，提高效率。
- **异步响应处理:** 支持异步响应处理，更好地配合异步流程。
- **高性能:** 异步特性使其在处理大量并发请求时表现出色，适用于高性能的异步 Web 应用。
- **WebSocket 支持:** 提供对 WebSocket 的支持，方便实现实时双向通信。
- **完整的文档:** 提供详细的官方文档，包含丰富的例子和用法说明。

## 安装

```bash
pip install aiohttp
```

## 使用

### 发送异步 GET 请求

```python
import aiohttp
import asyncio


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# Example usage:
# result = asyncio.run(fetch_data('https://www.example.com'))
# print(result)

```

### 发送异步 POST 请求

```python
import aiohttp
import asyncio


async def send_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.text()

# Example usage:
# result = asyncio.run(send_data('https://www.example.com', {'key': 'value'}))
# print(result)

```

## 工具类封装

参考`util_aiohttp.py`

```python
from util_aiohttp import AiohttpUtil

util_aiohttp = AiohttpUtil()
response = asyncio.run(util_aiohttp.get('https://www.example.com'))
print(response)
util_aiohttp.close_session()

```