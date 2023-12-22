# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@version    : v1.0
@author     : fangzheng
@contact    : fangzheng@rp-pet.cn
@software   : PyCharm
@filename   : util_pymysql.py
@create time: 2023/12/22 2:33 PM
@modify time: 2023/12/22 2:33 PM
@describe   : 
-------------------------------------------------
"""
import pymysql
from sshtunnel import SSHTunnelForwarder


class MySQL:
    def __init__(self, db_config, ssh_tunnel=None):
        self.dbconfig = db_config
        if ssh_tunnel:
            ssh_tunnel.start()
            self.dbconfig['host'] = ssh_tunnel.local_bind_host
            self.dbconfig['port'] = ssh_tunnel.local_bind_port
        self._init()

    def _init(self):
        try:
            self.connect = pymysql.connect(
                host=str(self.dbconfig['host']),
                port=self.dbconfig['port'],
                user=str(self.dbconfig['username']),
                passwd=str(self.dbconfig['password']),
                db=str(self.dbconfig['db']),
                charset=str(self.dbconfig['charset'])
            )
            self.cursor = self.connect.cursor()
            return True
        except Exception as err:
            raise Exception("MySQL Connection error", err)

    def get_conn(self):
        if self.connect:
            return self.connect
        else:
            self._init()
            return self.connect

    def close_conn(self):
        if self.connect:
            self.connect.close()

    def query(self, sql, param=None):
        """
        Query data
        :param sql:
        :param param:
        :param size: Number of rows of data you want to return
        :return: List of fetched rows or None if error occurs
        """
        try:
            with self.connect.cursor(cursor=pymysql.cursors.DictCursor) as cur:
                cur.execute(sql, param)
                rows = cur.fetchall()
                return rows
        except Exception as e:
            self.connect.rollback()
            raise Exception(f"Database query failed: {e}")

    def execute(self, sql):
        """
        exec DML：INSERT、UPDATE、DELETE
        :param sql: dml sql
        :return: Number of rows affected
        """
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise Exception(f"Database execute failed: {e}")
        else:
            return self.cursor.rowcount

