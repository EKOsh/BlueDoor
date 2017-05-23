#!/usr/bin/env python
# -*- coding: utf-8 -*-
from easygui import *
import configparser
config = configparser.ConfigParser(allow_no_value=True)
config.read('weed.ini')
global item
global summ
global allsumm
allsumm = 0
from peewee import *
db = SqliteDatabase('BDdb.db')
class SALES(Model):
    name = CharField()
    amount = CharField()
    cost = CharField()

    class Meta:
        database = db

db.connect()

def buy(item):
	msg = "Enter amount and price"
	title = item
	fieldNames = ["Amount","Price"]
	fieldValues = []  # we start with blanks for the values
	fieldValues = multenterbox(msg,title, fieldNames)
	am = int(fieldValues[0])
	pr = int(fieldValues[1])
	summ = am * pr
	sale = SALES.create(name = item, amount = am, cost = summ)
	sale.save()
	print('Amount is {}G, price is {}$. This item = {}$'.format(am, pr, summ))
	return summ
while 1:	
	msg ="Select item type and press OK"
	title = "Blue Door"		
	choices = config.sections()
	command = choicebox(msg, title, choices)
	print(command)
	
	if command == 'Indica':
		msg = 'Select strain and press OK'
		choices = config[command]
		item = choicebox(msg, title, choices)
		
	if command == 'Sativa':
		msg = 'Select strain and press OK'
		choices = config[command]
		item = choicebox(msg, title, choices)
		
	if command == 'Exit':
		break
	cost = buy(item)
	allsumm = allsumm + cost
	answer = ynbox('Same customer?', 'Warning', ('Yes', 'No'))
	if answer == 0:
		msgbox('Total is: {}$'.format(allsumm))
		allsumm = 0

	
	print(item)
