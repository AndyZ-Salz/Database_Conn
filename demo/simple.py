# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : main
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : 
---------------------------------------
"""

# History:
# 2021/8/27: Create
import link_auth_template
from DB_connect.DB_conn import DatabaseConnect

Auth = link_auth_template.DB_AUTH
print(Auth)

if __name__ == '__main__':
    # Connect to an existing database
    # Open a cursor to perform database operations

    # link = DatabaseConnect("host=localhost port=5432 dbname=test user=postgres password=sqlpass")
    # link = DatabaseConnect(host="localhost", port="5432", dbname="test", user="postgres", password="sqlpass")
    link = DatabaseConnect.init_by_auth(Auth)

    # open Log
    link.set_log(True)

    # Query the database and obtain data as Python objects
    print(link.select('*', 'ec_type_d', "type_g = '电容'"))

    # Make the changes to the database persistent
    # Close communication with the database
    del link
