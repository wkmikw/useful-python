#coding=utf-8
#python die_visual.py
from die import Die 

die = Die()
#save in a list
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)