#coding=utf-8
#python highs_lows.py

import csv
from matplotlib import pyplot as plt 
from datetime import datetime

def FtoC(degree):
	return(round(((int(degree)-32)/1.8),1))

filename = 'weather.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs ,lows= [], [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		highs.append(FtoC(row[1]))
		lows.append(FtoC(row[2]))

	#print(highs)

#plot data
fig = plt.figure(dpi=141, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#settings of fig
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()