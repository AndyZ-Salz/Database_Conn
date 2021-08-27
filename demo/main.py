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

Auth = link_auth_template.DB_AUTH

if __name__ == '__main__':
    import psycopg2

    # Connect to an existing database
    print(Auth)
    conn = psycopg2.connect(host=Auth['host'], port=Auth['port'], dbname=Auth['dbname'], user=Auth['user'],
                            password=Auth['password'])
    # conn = psycopg2.connect(host="localhost", port="5432", dbname="test", user="postgres", password="sqlpass")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM ec_type_g;")
    print(cur.fetchall())

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
