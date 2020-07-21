#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

connection = pymysql.connect(host="192.168.0.149",
                       user="workArhNet",
                       password="ebuciyShmel",
                       db="homeEvilCorp",
                       charset='utf8',
                       port=3306)
cursor = connection.cursor()   
sql =  "Insert into users (id, ip, mac, fullName, position, email, password) values (%s, %s, %s, %s, %s, %s, %s)"
     
    # Выполнить sql и передать 3 параметра.
cursor.execute(sql, (1, '192.168.0.109', '90:48:9a:bf:cb:b9', 'Eliseev A.S.', 'CEO', 'eliseevCEO@evilcorp', 'pizdatyipass') )
     
connection.commit() 
connection.close()
