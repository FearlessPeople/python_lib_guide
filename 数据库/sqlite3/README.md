# sqlite3

## 介绍

`sqlite3` 是 Python 中用于操作 SQLite 数据库的标准库。SQLite 是一种嵌入式数据库引擎，它是一个轻量级的数据库系统，无需独立的服务器进程，可以直接访问数据库文件。

## 官网地址
[SQLite官网](https://www.sqlite.org/index.html)

## 安装

`sqlite3` 实际上是 Python 标准库的一部分，所以无需pip安装，除非你使用的是特定的第三方包装。在大多数情况下，你只需导入标准库中的 sqlite3 模块即可开始使用。

## 使用案例

```python
import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('example.db')

# 创建一个游标对象来执行SQL语句
cursor = conn.cursor()

# 执行一些SQL操作...

# 提交更改并关闭连接
conn.commit()
conn.close()
```

## 工具类封装

参考`util_sqlite.py`

```python

# 创建实例并连接数据库
db = SQLiteDB()

```