#!/usr/bin/env python
# -*- coding: utf-8 -*-
import CreateConnect
import pymysql

def choiceTable():
	option = CreateConnect.getArgument()
	connect = CreateConnect.createConnect(option)
	cursor = connect.cursor()
	sqlReqest = 'show tables'
	cursor.execute(sqlReqest)
	tabList = cursor.fetchall()
	for item in tabList:
		print(item)
	
	
	return connect

def choiceOperation():
	connect = choiceTable()
	nameTable = input('[*] Укажите имя таблицы: ')
	print('1)Добавить запись\n2)Удалить запись\n3)Редатировать запись\n4)Прочитать таблицу')
	choiceInput = input('[*] Укажите Операцию (цифрой): ')
	try:
		cursor = connect.cursor()
		sql = 'show columns from %s' % nameTable
		cursor.execute(sql)
		result = cursor.fetchall()
		#парсим нахуй вывод шоб получить имена таблиц и их кол-во
		nameColumn = []
		for item in result:
			nameColumn.append(item[0])
		print(nameColumn)

	except pymysql.err.ProgrammingError as error:
		if '1146' in str(error):
			print('[!] Таблицы ' + nameTable + ' не существует')
			connect.close()
			choiceOperation()
	
	dataInput = input('[*] Укажите данные формата id:1 name:Nick ')
	data = dataInput.split(' ')
	dataKey = []
	dataVel = []
	for item in data:
		item = item.split(':')
		dataKey.append(item[0])
		dataVel.append(item[1])

	if choiceInput == '1':
		try:
			sqlReqest = 'insert into ' + nameTable + str(dataKey) + ' values ' + str(dataVel)
		#	sqlReqest = 'Insert into %s' %nameTable '(%s)' %nameColumn ' values (%s, %s, %s, %s, %s, %s)'
			cursor.execute(sqlReqest)    
			connection.commit()
		except pymysql.err.ProgrammingError as error:
			if '1064' in str(error):
				print('[!] Ошибка в синтаксисе, неверно указан ключ')
				connect.close()
				choiceOperation()
	elif choiseInput == '2':
		pass
	elif choiseInput == '3':
		pass
	elif choiseInput == '4':
		pass
	 

choiceOperation()