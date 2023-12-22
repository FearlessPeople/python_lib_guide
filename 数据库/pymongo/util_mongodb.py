# -*- coding: utf-8 -*-

from pymongo import MongoClient


class MongoDBTool:
    def __init__(self, host='localhost', port=27017, db_name='test'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many(self, collection_name, data_list):
        collection = self.db[collection_name]
        result = collection.insert_many(data_list)
        return result.inserted_ids

    def find(self, collection_name, query=None):
        collection = self.db[collection_name]
        if query:
            cursor = collection.find(query)
        else:
            cursor = collection.find()

        return list(cursor)

    def update_one(self, collection_name, query, data):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': data})

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def drop_collection(self, collection_name):
        collection = self.db[collection_name]
        collection.drop()

    def close_connection(self):
        if self.client:
            self.client.close()
