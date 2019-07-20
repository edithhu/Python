"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/7 15:45
 @File    : DB_operated.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""


import re
import traceback
import json
import cx_Oracle


class Trans():
    def __init__(self):
        self.json_path = "json2mongo.json"
        self.mysql_path = "csv2mysql.csv"
        self.oracle_path = "csv2oracle.csv"
        self.oracle_localhost = cx_Oracle.connect('app_common_service/Tebon@20180522@192.168.2.49:1521/orcl')    # 链接信息：localhost:1521/orcl，在数据库中右键属性，查看链接详细信息

    def csv2oracle(self):
        print("connect to oracle...")
        try:
            # 1. 链接Oracle数据库
            conn = self.oracle_localhost
            cursor = conn.cursor()

            # 2. 查询数据
            sql = "select * from KCB_INFO_AND_LISTED_INFO where row_count =1"
            cursor.execute(sql)
            allData = cursor.fetchall()  # cursor.fetchone()
            for data in allData:
                print(data)

            # # 3. 插入、更新、删除  主要区别在于sql不同
            # def sqlDML(sql, conn):
            #     cursor = conn.cursor()
            #     cursor.execute(sql)
            #     cursor.close()
            #     conn.commit()

            conn.commit()
            cursor.close()
            conn.close()
        except:
            conn.rollback()

if __name__ == '__main__':
    trans = Trans()
    # trans.json2mongodb()
    # trans.csv2mysql()
    trans.csv2oracle()


