#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('BDdb.db')


class SALES(Model):
    name = CharField()
    amount = CharField()
    price = CharField()
    cost = CharField()
    time = CharField()

    class Meta:
        database = db

db.connect()


db.create_tables([SALES])
