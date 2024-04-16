# -*- coding: utf-8 -*-

from pymongo import MongoClient


class MongoDBTool:
    """
    MongoDB工具类
    """

    def __init__(self, host='localhost', port=27017, db_name='test'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        """
        连接
        :return:
        """
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]

    def insert_one(self, collection_name, data_dict):
        """
        插入一条数据

        Example:
        data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
        mg.insert_one('users', data)

        :param collection_name:
        :param data_dict: dict对象
        :return:
        """
        collection = self.db[collection_name]
        return collection.insert_one(data_dict)

    def insert_many(self, collection_name, data_list):
        """
        插入多条数据
        :param collection_name:
        :param data_list: list对象
        :return:
        """
        collection = self.db[collection_name]
        insert_result = collection.insert_many(data_list)
        return insert_result.inserted_ids

    def find(self, collection_name, condition=None):
        """
        查询

        result = mg.find('users', query={"name": "Alice"})
        for item in result:
            print(item)
        :param collection_name:
        :param condition:
        :return:
        """
        collection = self.db[collection_name]
        if condition:
            cursor = collection.find(condition)
        else:
            cursor = collection.find()

        return list(cursor)

    def update_one(self, collection_name, condition, update_data):
        """
        更新一条记录

        update_filter = {"name": "Alice"}
        update_data = {"age": 31}
        mg.update_one('users', update_filter, update_data)
        :param collection_name:
        :param condition: 更新条件dict类型
        :param update_data: 更新数据dict类型
        :return:
        """
        collection = self.db[collection_name]
        return collection.update_one(condition, {'$set': update_data})

    def delete_one(self, collection_name, condition):
        """
        删除数据

        delete_query = {"name": "Alice"}
        mongo_tool.delete_one('users', delete_query)
        :param collection_name:
        :param condition: 删除条件dict类型
        :return:
        """
        collection = self.db[collection_name]
        return collection.delete_one(condition)

    def drop_collection(self, collection_name):
        """
        删除文档
        :param collection_name:
        :return:
        """
        collection = self.db[collection_name]
        collection.drop()

    def close_connection(self):
        """
        关闭连接
        :return:
        """
        if self.client:
            self.client.close()


mg = MongoDBTool()

if __name__ == '__main__':

    # 使用示例
    # 创建实例并连接数据库
    # local_mongo = MongoDBTool(host='localhost', port=27017, db_name='test')

    # 插入数据
    data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    mg.insert_one('users', data)

    # 查询数据
    result = mg.find('users', condition={"name": "Alice"})
    for item in result:
        print(item)

    # 更新数据
    query = {"name": "Alice"}
    update_data = {"age": 31}
    mg.update_one('users', query, update_data)

    # 删除数据
    # delete_query = {"name": "Alice"}
    # mongo_tool.delete_one('users', delete_query)

    # 关闭连接
    mg.close_connection()
