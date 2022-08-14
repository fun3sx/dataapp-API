# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:17:14 2022

@author: User
"""

from dataapi1.database import db

class MortgageModel(db.Model):
	month = db.Column(db.String(100), nullable=False,primary_key=True)
	value = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return f"Entry(month = {month}, value = {value})"
