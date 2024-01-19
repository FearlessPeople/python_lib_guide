# Peewee

## 介绍
[Peewee](http://docs.peewee-orm.com/) 是一个轻量级的Python ORM（对象关系映射）库，用于简化与关系型数据库的交互。它提供简单而强大的API，支持多种数据库后端，包括SQLite、MySQL、PostgreSQL等。

## 安装
你可以使用以下命令通过 pip 安装 Peewee：

```bash
pip install peewee
```

## 使用

```python
from peewee import SqliteDatabase, Model, CharField

# 创建 SQLite 数据库连接
db = SqliteDatabase('my_database.db')

# 定义基础模型类
class BaseModel(Model):
    class Meta:
        database = db

# 示例模型
class Person(BaseModel):
    name = CharField()

# 连接数据库并创建表格
db.connect()
db.create_tables([Person])

# 创建并插入一条记录
person = Person.create(name='John Doe')
# 查询所有记录
people = Person.select()
# 查询特定条件的记录
selected_people = Person.select().where(Person.name == 'John Doe')
# 更新记录
person = Person.get(Person.name == 'John Doe')
person.name = 'Jane Doe'
person.save()
# 删除记录
person = Person.get(Person.name == 'Jane Doe')
person.delete_instance()

```