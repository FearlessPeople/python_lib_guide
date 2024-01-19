# httpie

## 简介
[httpie](https://github.com/httpie/httpie) 是一个命令行 HTTP 客户端，提供直观的命令行界面用于测试和调试 HTTP 请求。

## 特性
- 直观的命令行界面
- 支持 HTTP 方法
- 语法高亮
- 常用认证方式支持
- 请求和响应数据格式化输出
- 自定义请求头
- 支持文件上传
- 插件系统

## 安装

```bash
pip install httpie
```

## 使用

```bash
# 发送 GET 请求
http GET https://www.example.com

# 发送 POST 请求
http POST https://www.example.com key=value

# 自定义请求头
http GET https://www.example.com User-Agent:Mozilla/5.0

# 文件上传
http POST https://www.example.com/upload file@/path/to/file

```