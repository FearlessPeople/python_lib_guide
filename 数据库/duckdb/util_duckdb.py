# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_duckdb.py
@create time: 2024/1/19 10:37 AM
@modify time: 2024/1/19 10:37 AM
@describe   : 
-------------------------------------------------
"""

import duckdb


class DuckDBUtil:
    def __init__(self, database=':memory:'):
        self.conn = duckdb.connect(database=database, read_only=False)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        create_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
        self.cursor.execute(create_query)

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in data[0]])
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.executemany(insert_query, data)
        self.conn.commit()

    def select_data(self, table_name):
        select_query = f"SELECT * FROM {table_name}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def update_data(self, table_name, set_values, condition):
        set_clause = ', '.join([f"{column} = ?" for column in set_values.keys()])
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(update_query, list(set_values.values()))
        self.conn.commit()

    def delete_data(self, table_name, condition):
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
