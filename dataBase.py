#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

connection = pymysql.connect(host="localhost",
                       user="devArhNet",
                       password="ebuciyShmel",
                       db="homeEvilCorp",
                       charset='utf8',
                       port=3306)
with connection.cursor() as cursor:
	sql = 'select * from usersEvilCorp'
	cursor.execute(sql)
	for row in cursor:
		print(row)
		connection.close()
