# httplib2

## 简介
[httplib2](https://github.com/httplib2/httplib2) 是一个全功能的HTTP客户端库，用于发送HTTP请求和处理响应。它基于Python的httplib模块，提供了一些额外的功能和改进。

## 特性
- 支持持久连接和连接池
- 支持缓存机制
- 支持代理
- 支持基本的认证和摘要认证
- 支持 gzip 和 deflate 压缩
- 提供丰富的异常处理机制


## httplib2 vs requests

### 不同点

**httplib2**
- **连接池和持久连接:** `httplib2` 支持连接池和持久连接，可以在多个请求之间保持长连接，提高效率。
- **缓存机制:** 提供了缓存机制，可以缓存先前的请求和响应，避免重复的网络请求。
- **代理支持:** 支持使用代理进行请求。
- **基本认证和摘要认证:** 提供基本认证和摘要认证的支持。

**requests**
- **广泛使用:** `requests` 是一个广泛使用的 HTTP 请求库，简单易用，适合绝大多数场景。
- **丰富的特性:** 提供了丰富的特性，包括文件上传、会话管理、自动重定向等。
- **生态系统:** 有庞大的生态系统和活跃的社区支持。

### 优缺点

**httplib2**

- **优点:**
  - 支持持久连接和连接池。
  - 具有缓存机制，可以减少重复请求。
  - 提供了一些高级特性，如代理、认证等。

- **缺点:**
  - 较小的社区和相对较少的活跃度。
  - 在某些方面可能不如 `requests` 方便。

**requests**
- **优点:**
  - 广泛使用，社区活跃度高，文档丰富。
  - 提供了丰富的特性，易于上手。

- **缺点:**
  - 不支持持久连接和连接池（不适合大量的长连接请求）。
  - 缓存机制相对简单。

**结论**

选择 `httplib2` 还是 `requests` 取决于具体的需求和使用场景。如果需要高级特性、广泛的社区支持和文档丰富，推荐使用 `requests`。如果对持久连接和缓存有特殊需求，或者在小规模项目中使用，`httplib2` 也是一个不错的选择。


## 安装

```bash
pip install httplib2
```

## 使用

```python
import httplib2

# 发送 GET 请求
http = httplib2.Http()
response, content = http.request('https://www.example.com', 'GET')
print(content)

# 发送 POST 请求
data = {'key': 'value'}
response, content = http.request('https://www.example.com', 'POST', body=urllib.parse.urlencode(data))
print(content)

```

## 工具类封装

```python
from util_httplib2 import Httplib2Util

util_httplib2 = Httplib2Util()
response = util_httplib2.get('https://www.example.com')
print(response)
util_httplib2.close_http()

```