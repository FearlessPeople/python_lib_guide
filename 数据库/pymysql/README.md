# pymysql

## 介绍
[pymysql](https://pypi.org/project/PyMySQL/) 是一个用于连接 MySQL 数据库的 Python 模块。它提供了对 MySQL 数据库的高效、简便的操作方式，使得在 Python 中与 MySQL 数据库进行交互变得容易。

## 安装

```bash
pip install pymysql
```

## 使用

```python
import pymysql

# 连接到数据库
conn = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='dbname',
    port=3306
)

# 创建一个游标对象来执行SQL语句
cursor = conn.cursor()

# 执行一些SQL操作...

# 提交更改并关闭连接
conn.commit()
conn.close()

```

## 工具类封装

参考`util_pymysql.py`

```python

from util_pymysql import MySQL
from sshtunnel import SSHTunnelForwarder

dbconfg = {
    'host': '127.0.0.1',
    'username': 'root',
    'password': '123456',
    'port': 3306,
    'db': 'test',
    'charset': 'utf8mb4'
}
server = SSHTunnelForwarder(
    ssh_address_or_host=('127.0.0.1', 45535),
    ssh_username='admin',
    ssh_password='2893823',
    local_bind_address=('127.0.0.1', 9704),
    remote_bind_address=(dbconfg['host'], dbconfg['port'])
)

# 使用堡垒机
db = MySQL(dbconfg, ssh_tunnel=server)
# 不使用堡垒机
db = MySQL(dbconfg)

db.query("select * from user")
```