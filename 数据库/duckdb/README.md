# DuckDB

## 介绍
[DuckDB](https://github.com/duckdb/duckdb) 是一个高性能的分析型数据库管理系统，它被设计用于支持大规模数据分析。DuckDB 提供了快速的查询性能和低延迟，同时具备嵌入式和分布式部署的能力。具有以下特点：

- 高性能： DuckDB 专注于提供快速的查询性能和低延迟。它在大规模数据分析场景中表现出色，适用于需要高吞吐量和低查询延迟的应用。
- 嵌入式： DuckDB 可以作为一个嵌入式数据库直接集成到应用程序中。这使得在应用程序内部进行数据分析变得更加便捷。
- 支持 SQL： DuckDB 提供了标准的 SQL 查询语言支持，使得用户可以使用熟悉的语法进行数据查询和操作。
- 内存管理： DuckDB 具有高效的内存管理机制，允许在有限的内存资源下执行大规模的查询操作。
- 支持多种数据格式： DuckDB 可以处理多种数据格式，包括 Parquet、Arrow 和 CSV 等，使得数据导入和导出更加灵活。
- 兼容性： DuckDB 兼容 PostgreSQL 的网络协议，因此可以通过现有的 PostgreSQL 客户端进行连接和交互。
- 跨平台： DuckDB 支持多个平台，包括 Linux、macOS 和 Windows，可以轻松部署到不同的操作系统上。
- 开源： DuckDB 是一个开源项目，其源代码托管在 GitHub 上，用户可以查看源码、提出问题和参与贡献。

以上特点使得 DuckDB 成为一个灵活、高性能的数据库系统，适用于各种数据分析和查询场景。详细信息请参阅 DuckDB 官方文档。

## 安装
DuckDB 提供了多种安装方式，包括二进制发行版、源码编译和使用包管理工具。以下是使用pip安装的示例：

```bash
brew install duckdb
```

## 使用


```python
import duckdb

# 连接到 DuckDB 数据库
conn = duckdb.connect(database=':memory:', read_only=False)

# 创建一个游标对象来执行SQL语句
cursor = conn.cursor()

# 执行一些SQL操作...

# 关闭连接
conn.close()

```

## 工具类封装

参考`util_duckdb.py`

```python
# 创建 DuckDBUtil 实例
duckdb_util = DuckDBUtil()

# 创建表格
duckdb_util.create_table('users', ['id INTEGER PRIMARY KEY', 'username TEXT NOT NULL', 'email TEXT NOT NULL'])

# 插入数据
data_to_insert = [(1, 'john_doe', 'john@example.com'), (2, 'jane_doe', 'jane@example.com')]
duckdb_util.insert_data('users', data_to_insert)

# 查询数据
result = duckdb_util.select_data('users')
print(result)

# 更新数据
update_values = {'username': 'new_username'}
duckdb_util.update_data('users', update_values, 'id = 1')

# 查询更新后的数据
result_after_update = duckdb_util.select_data('users')
print(result_after_update)

# 删除数据
duckdb_util.delete_data('users', 'id = 2')

# 查询删除后的数据
result_after_delete = duckdb_util.select_data('users')
print(result_after_delete)

# 关闭连接
duckdb_util.close_connection()
```