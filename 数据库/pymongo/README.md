# 使用案例

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