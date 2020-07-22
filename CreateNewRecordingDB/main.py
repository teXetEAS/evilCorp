#!/usr/bin/env python
# -*- coding: utf-8 -*-

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