# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : DB_conn
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : class
---------------------------------------
"""

# History:
# 2021/8/31: Create

import time
import psycopg2
import DB_connect.DM as DM, DB_connect.DBM as DBM
import private_setting.link_auth


class DatabaseConnect:
    """

    """
    link_auth = []
    log_status = False
    log_direction = None

    def set_log(self, status: bool, direction=None):
        self.log_status = status
        self.log_direction = direction
        if status:
            print("-------------------------------\n\rThis is a DatabaseConnect class's object")
            print(self)
            print("-------------------------------\n\rNow, the LOG is on at " + time.asctime(
                time.localtime(time.time())))

    def log_handle(self, log_body: str):

        if self.log_status:
            if self.log_direction is None:
                print("LOG: " + log_body + " at " + time.asctime(time.localtime(time.time())))
            else:
                pass

    def __init__(self, dsn=None, connection_factory=None, cursor_factory=None, **kwargs):
        self.conn = psycopg2.connect(dsn=dsn, connection_factory=connection_factory, cursor_factory=cursor_factory,
                                     **kwargs)
        self.cur = self.conn.cursor()
        self.log_handle("connection open")

        # another init

    @classmethod
    def init_by_auth(cls, auth: dict):
        return cls(host=auth['host'], port=auth['port'], dbname=auth['dbname'], user=auth['user'],
                   password=auth['password'])

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.log_handle("connection closed")

    def __str__(self):
        return str(self.conn) + "\n\r" + str(self.cur)

    def cur_execute(self, query, vars=None):
        self.cur.execute(query, vars)
        self.log_handle("query:/" + query.as_string(self.conn) + "/")
        return self.cur.fetchall()

    # DM part
    def select(self, what, table: str, where=None):
        SQL_query = DM.select_sql(what, table, where)
        return self.cur_execute(SQL_query)


if __name__ == '__main__':
    import link_auth_template

    Auth = link_auth_template.DB_AUTH
    # Auth = private_setting.link_auth.DB_FTP

    # link = DatabaseConnect("host=localhost port=5432 dbname=test user=postgres password=sqlpass")
    # link = DatabaseConnect(host="localhost", port="5432", dbname="test", user="postgres", password="sqlpass")
    link = DatabaseConnect.init_by_auth(Auth)
    link.set_log(True)

    # buildin func
    # print(link.cur_execute("SELECT * FROM ec_type_d"))
    # print(link.cur_execute("SELECT * FROM ec_type_d WHERE type_g = %s",['电容']))

    # DM select
    print(link.select('type_d', 'ec_type_d',"type_g = '电容'"))
    print(link.select('type_g', 'ec_type_d'))
    print(link.select('*', 'ec_type_d',"type_g = '电容'"))
