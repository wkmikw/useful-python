#coding=utf-8
#python die.py
from random import randint

class Die(object):
	"""骰子"""
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)
