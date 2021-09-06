# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : DM
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Data Management
---------------------------------------
"""

# History:
# 2021/8/31: Create


import psycopg2
from psycopg2 import sql


def select_sql(what, table: str, where=None):
    if what == '*':  # select *
        if where is None:  # No Where
            SQL_query = sql.SQL("SELECT * FROM {tbl}").format(
                tbl=sql.Identifier(table)
            )
        else:  # Where
            # TODO consider to support multi-paras
            raw_SQL = "SELECT * FROM {tbl} WHERE "
            raw_SQL += where

            SQL_query = sql.SQL(raw_SQL).format(
                tbl=sql.Identifier(table)
            )

    else:  # select not *
        if where is None:  # No Where
            SQL_query = sql.SQL("SELECT {col} FROM {tbl}").format(
                col=sql.Identifier(what),
                tbl=sql.Identifier(table)
            )
        else:  # Where
            # TODO consider to support multi-paras
            raw_SQL = "SELECT {col} FROM {tbl} WHERE "
            raw_SQL += where

            SQL_query = sql.SQL(raw_SQL).format(
                col=sql.Identifier(what),
                tbl=sql.Identifier(table)
            )

    return SQL_query


def insert_sql():
    pass


def update_sql():
    pass


def delete_sql():
    pass


if __name__ == '__main__':
    print(select_sql('*', 'ec_type_d', "type_g = '电容'"))
