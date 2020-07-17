#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

connection = pymysql.connect(host="192.168.0.122",
                       user="devWork@",
                       password="iLikeOpenSuse",
                       db="homeDataBaseEvilCorp",
                       charset='utf8',
                       port=3306)
with connection.cursor() as cursor:
	sql = 'select * from "t1"'
	cursor.execute(sql)
	for row in cursor:
		print(row)
		connection.close()