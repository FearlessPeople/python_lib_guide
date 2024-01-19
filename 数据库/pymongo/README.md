
# pymongo库

## 介绍
[pymongo](https://pypi.org/project/pymongo/) 是一个用于连接 MongoDB 数据库的 Python 模块。它提供了在 Python 中与 MongoDB 数据库进行交互的工具，支持灵活的文档存储和查询。

## 安装

```bash
pip install pymongo
```

## 使用

```python
from pymongo import MongoClient

# 连接到数据库
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 插入一条数据
data = {'name': 'John Doe', 'email': 'john@example.com'}
result = collection.insert_one(data)

# 打印插入的数据的ID
print('Inserted ID:', result.inserted_id)

# 关闭连接
client.close()

```

## 工具类封装

参考`util_mongodb.py`

```python

# 使用示例
# 创建实例并连接数据库
local_mongo = MongoDBTool(host='localhost', port=27017, db_name='test')

# 插入数据
data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
local_mongo.insert_one('users', data)

# 查询数据
result = local_mongo.find('users', query={"name": "Alice"})
for item in result:
    print(item)

# 更新数据
query = {"name": "Alice"}
update_data = {"age": 31}
local_mongo.update_one('users', query, update_data)

# 删除数据
# delete_query = {"name": "Alice"}
# mongo_tool.delete_one('users', delete_query)

# 关闭连接
local_mongo.close_connection()

```