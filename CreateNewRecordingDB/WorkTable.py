#!/usr/bin/env python
# -*- coding: utf-8 -*-
import CreateConnect
import pymysql
import sys

def choiceTable():
	option = CreateConnect.getArgument()
	connect = CreateConnect.createConnect(option)
	try:
		cursor = connect.cursor()
		sqlReqest = 'show tables'
		cursor.execute(sqlReqest)
		tabList = cursor.fetchall()
		for item in tabList:
			print(item)
		return connect
	except AttributeError:
		sys.exit()

def choiceOperation():
	connect = choiceTable()
	try:
		nameTable = input('[*] Укажите имя таблицы: ')
		try:
			cursor = connect.cursor()
			sql = 'show columns from %s' % nameTable
			cursor.execute(sql)
			column = cursor.fetchall()
			for item in column:
				print('{:<12} : {:<12}'.format(item[0], item[1]))
		except pymysql.err.ProgrammingError as error:
			if '1146' in str(error):
				print('[!] Таблицы ' + nameTable + ' не существует')
				connect.close()
				choiceOperation()
		except KeyboardInterrupt:
			print('\n[.] Выход из программы')
			connect.close()
			sys.exit()
		print('\n1)Добавить запись\n2)Удалить запись\n3)Редатировать запись\n4)Прочитать таблицу')
		choiceInput = int(input('[*] Укажите Операцию (цифрой): '))
	except KeyboardInterrupt:
		print('\n[.] Выход из программы')
		connect.close()
		sys.exit()
	except ValueError:
		print("[!] Укажите число")
		connect.close()
		choiceOperation()

	#Создание новой записи
	if choiceInput == 1:
		whileCheac = True
		while whileCheac:
			try:
				dataInput = input('[*] Укажите данные формата id:1 name:"Nick" ')
				data = dataInput.split(' ')
				dataKey = []
				dataVel = []
				for item in data:
					item = item.split(':')
					dataKey.append(item[0])
					dataVel.append(item[1])
			except KeyboardInterrupt:
				print('\n[.] Выход из программы')
				connect.close()
				sys.exit()

			try:
				sqlReqest = 'insert into ' + nameTable + '(' + ", ".join(dataKey) + ') values(' + ", ".join(
					dataVel) + ')'
				cursor.execute(sqlReqest)
				connect.commit()
			except pymysql.err.ProgrammingError as error:
				if '1064' in str(error):
					print('[!] Ошибка в синтаксисе, неверно указанно значение')
			except pymysql.err.IntegrityError as error:
				if '1062' in str(error):
					print('[!] Ошибка ввода данных, повторяется запись')
			except pymysql.err.OperationalError as error:
				if '1054' in str(error):
					print("[!] не верно указано имя столбца")
			else:
				print('[+] Запись данных успешно выполнена')

			try:
				userInput = input('Продолжить? (y/n)').lower()
				if userInput == 'n':
					whileCheac = False
					connect.close()
					choiceOperation()
				else:
					whileCheac = True
			except KeyboardInterrupt:
				print('\n[.] Выход из программы')
				connect.close()
				sys.exit()

	#Удаление записи ДОДЕЛАТЬ
	elif choiceInput == 2:
		whileCheac = True
		while whileCheac:
			idInput = input('[*] Укажите ID записи которую нужно удалить: ')
			try:
				sqlRequst = 'delete from ' + nameTable + ' where mac=' + idInput
				cursor.execute(sqlRequst)
				connect.commit()
			except pymysql.err.ProgrammingError as error:
				if '1064' in str(error):
					print('[!] Ошибка в синтаксисе, неверно указанно значение')



			try:
				userInput = input('Продолжить? (y/n)').lower()
				if userInput == 'n':
					whileCheac = False
					connect.close()
					choiceOperation()
				else:
					whileCheac = True
			except KeyboardInterrupt:
				print('\n[.] Выход из программы')
				connect.close()
				sys.exit()
	#
	elif choiceInput == '3':
		pass
	#чтение данных
	elif choiceInput == 4:
		whileCheac = True
		while whileCheac:
			sqlRequst = 'select id, ip, fullName, position, email from ' + nameTable
			cursor.execute(sqlRequst)
			resalt = cursor.fetchall()
			for item in resalt:
				print(str(item))
			try:
				userInput = input('[*] Найти определенного пользователя по ID? (y/n): ')
				if userInput == 'n':
					connect.close()
					choiceOperation()
			except KeyboardInterrupt:
				print('\n[.] Выход из программы')
				connect.close()
				sys.exit()
			else:
				try:
					search = input('Укажите ID записи: ')
					sqlRequst = 'select id, ip, fullName, position, email from ' + nameTable + ' where id=' + search
					cursor.execute(sqlRequst)
					resalt = cursor.fetchall()
					if len(resalt) == 0:
						print('[!] ID ' + search + ' не существует')
						userInput = input('Продолжить? (y/n): ')
						if userInput == 'n':
							connect.close()
							sys.exit()
					else:
						print('[+] Запись ' + str(resalt))
						connect.close()
						choiceOperation()
				except KeyboardInterrupt:
					print('\n[.] Выход из программы')
					connect.close()
					sys.exit()



	else:
		print('[!] Неверная операция')


choiceOperation()