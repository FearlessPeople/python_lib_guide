# SQLObject
## 介绍
[SQLObject](https://sqlobject.org/) 是一个简单而强大的Python ORM库，用于简化与关系型数据库的交互。它提供了高层次的对象接口，允许使用Python类和对象来映射数据库表。

**特点**

- **易用性：** 提供了简单而直观的API，降低了学习和使用的难度。
- **高层对象接口：** 使用Python类和对象来映射数据库表，提供了直观而易于理解的高层次对象接口。
- **支持多种数据库后端：** 支持多种数据库后端，包括但不限于 SQLite、MySQL、PostgreSQL。
- **自动化表格创建：** 具有自动创建表格的功能，简化了数据库初始化的流程。
- **轻量级：** 相对于一些更庞大的ORM库，SQLObject 是一个相对轻量级的库。
- **原生SQL支持：** 允许开发者使用原生SQL语句，提供更灵活的数据库操作。
- **丰富的文档：** 提供了详细且清晰的文档，包括入门指南、API文档等。

## 安装
你可以使用以下命令通过 pip 安装 SQLObject：

```bash
pip install SQLObject
```

## 使用

```python
from sqlobject import SQLObject, connectionForURI, StringCol, sqlhub

# 连接 SQLite 数据库
connection_string = 'sqlite:/:memory:'
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

# 示例模型
class Person(SQLObject):
    name = StringCol()
# 创建并插入一条记录
person = Person(name='John Doe')
person.sync()
# 更新记录
person = Person.selectBy(name='John Doe').getOne()
person.name = 'Jane Doe'
person.sync()
# 删除记录
person = Person.selectBy(name='Jane Doe').getOne()
person.destroySelf()

```