#coding=utf-8
#python die_visual.py
from die import Die 
import pygal

die_1 = Die()
die_2 = Die(10)
#save in a list
results = []
for roll_num in range(10000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#visual
hist = pygal.Bar()

hist.title = "Results of rolling  D6+D10 1000 times"
outnum = []
for i in range(2,max_result+1):
	outnum.append(str(i))
hist.x_labels = outnum
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

#print(frequencies)

