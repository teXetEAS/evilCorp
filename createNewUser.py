#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

def getArgument():
	pass

def createConnect():
	try:
		connection = pymysql.connect(host='192.168.0.149',
			user='workArhNet',
			password='ebuciyShmel',
			db='homeEvilCorp',
			charset='utf8',
			port=3306)
		print('[+] Соединение с ' + db + ' установленно')
		return connection
	except Error:
		print('[!] Ошибка соединения!!!!')
		connection.close()

def createNewUser(connection):
	while True:
		ipInput = input('ip: ')
		macInput = input('mac-address: ')
		nameInput = input('Ф.И.О.: ')
		postInput = input('Должность: ')
		mailInput = input('e-mail: ')
		passInput = input('Пароль: ')
		cursor = connection.cursor()   
		sql =  "Insert into users (ip, mac, fullName, position, email, password) values (%s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (ipInput, macInput, nameInput, postInput, mailInput, passInput))    
		connection.commit() 
		enterChoise = input("[?] Продолжить заполнение таблицы (y/n): ")
		if enterChoise == "y":
			pass
	connection.close()

connection = createConnect()
createNewUser(connection)
