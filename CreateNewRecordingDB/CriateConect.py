#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import optparse
import getpass

def getArgument():
	options = optparse.OptionParser()
	options.add_option('-H', '--host', dest='host', help='HOST(IP) удаленной базы данных')
	options.add_option('-u', '--user', dest='user', help='LOGIN администратора')
	options.add_option('-d', '--database', dest='database', help='Название базы данных')
	(option, argument) = options.parse_args()
	if not option.host:
		options.error('[!] Укажите адрес удаленного DB сервера')
	if not option.user:
		options.error('[!] Укажите логин пользователя удаленного DB сервера')
	if not option.database:
		options.error('[!] Укажите название базы данных к которой вы хотите подключится')
	return option

def createConnect(option):
	hostName = option.host
	userName = option.user
	dbName = option.database
	passName = getpass.getpass('Введите пароль пользователя базы данных: ')
	try:
		connection = pymysql.connect(host=hostName,
			user=userName,
			password=passName,
			db=dbName,
			charset='utf8',
			port=3306)
		print('[+] Соединение с ' + dbName + ' установленно')
		return connection
	except pymysql.err.OperationalError as e:
		print(e)
	except UnicodeEncodeError:
		print('[!] Не правильный логин/пароль (не верная кодировка)')
	#закрывать соединение после после манипуляций с бд
	#connection.close()
		

option = getArgument()
createConnect(option)