# httpx

## 简介

[httpx](https://www.python-httpx.org/) 是一个现代的异步HTTP客户端/服务器框架，支持异步和同步请求。它设计简单，易于使用，并提供了许多先进的特性。

**特性**

- 异步和同步请求支持
- 先进的连接池管理
- 支持 HTTP/1.1 和 HTTP/2
- 支持 WebSocket
- 自动识别 JSON 数据
- 请求和响应模型
- 异常处理
- 完善的文档

## 安装

```bash
pip install httpx
```

## 使用

```python
import httpx


# 异步 GET 请求
async def get(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


# 异步 POST 请求
async def post(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        return response.text

# Example usage:
# result = await get('https://www.example.com')
# print(result)

# result = await post('https://www.example.com', {'key': 'value'})
# print(result)

```

## 工具类封装

参考`util_httpx.py`

```python
from util_httpx import HttpxUtil

util_httpx = HttpxUtil()
response = util_httpx.get('https://www.example.com')
print(response)
util_httpx.close_client()
```