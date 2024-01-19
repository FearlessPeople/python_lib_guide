# requests

## 简介
[Requests](https://github.com/psf/requests) 是一个用于发送 HTTP 请求的 Python 库，它提供了简单而强大的 API，广泛用于处理网络请求。以下是 `requests` 库的一些常见用法：

**特性**

- **简洁的API:** 提供了直观和简单的 API，使得发送 HTTP 请求变得容易。
- **多种HTTP方法:** 支持多种 HTTP 方法，包括 GET、POST、PUT、DELETE 等。
- **请求和响应处理:** 提供了对请求和响应的丰富处理能力，包括状态码、头信息、内容等。
- **Session管理:** 支持使用 `Session` 对象管理会话，包括跨请求的状态保持和 cookie 处理。
- **SSL证书验证:** 允许自定义证书，支持 SSL 证书验证。
- **重定向和历史:** 自动处理重定向，并提供请求历史信息。
- **超时设置:** 允许设置超时时间，以避免请求等待时间过长。
- **异常处理:** 提供异常处理机制，方便捕获和处理请求过程中的异常情况。
- **文件上传和下载:** 支持简单的文件上传和下载操作。
- **完善的文档:** 有详细而清晰的官方文档，提供了丰富的例子和用法说明。


## 安装

```bash
pip install requests
```

## 使用

```python

# 发送 GET 请求
import requests

response = requests.get('https://www.example.com')
print(response.text)

# 发送 POST 请求
import requests

data = {'key': 'value'}
response = requests.post('https://www.example.com/post', data=data)
print(response.text)


```

## 工具类封装

```python
from util_requests import RequestsUtil

http = RequestsUtil()
response = http.get('https://www.example.com')
print(response.text)
http.close_session()

```
