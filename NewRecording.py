#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import optparse

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
	passName = getpass.getpass('Введите пароль пользователя базы данных')
	try:
		connection = pymysql.connect(host=hostName,
			user=userName,
			password=dbName,
			db=dbName,
			charset='utf8',
			port=3306)
		print('[+] Соединение с ' + db + ' установленно')
		return connection
	except Error:
		print('[!] Ошибка соединения!!!!')
		connection.close()

def main(connection):
	cheackWhile = True
	while cheackWhile:
		getArg = input('[*] Укажите флаг для дальнейшей работы (-h - Посмотреть список флагов) ')
		if getArg == '-nU':
			newRecording(connection)
		elif getArg == '-dU':
			deletRecording(connection)
		elif getArg == '-q':
			cheackWhile = False
		elif getArg == '-h':
			print('-nU\t\t\tСделать новую запись' + 
				'-dU\t\t\tУдалить запись' + 
				'-q\t\t\tЗакончить работу с данными')
		else:
			print('[!] Не корректный флаг')

def newRecording(connection):
	cheackWhile = True
	while cheackWhile:
		ipInput = input('ip: ')
		macInput = input('mac-address: ')
		nameInput = input('Ф.И.О.: ')
		postInput = input('Должность: ')
		mailInput = input('e-mail: ')
		passInput = input('Пароль: ')
		cursor = connection.cursor()   
		sql =  'Insert into users (ip, mac, fullName, position, email, password) values (%s, %s, %s, %s, %s, %s)'
		cursor.execute(sql, (ipInput, macInput, nameInput, postInput, mailInput, passInput))    
		connection.commit() 
		enterChoise = input('[?] Продолжить заполнение таблицы (y/n): ')
		if enterChoise != 'y':
			cheackWhile = False
	connection.close()

def deletRecording(connection):
	pass
	#удаление записи\пользователя


option = getArgument()
connection = createConnect(option)
main(connection)