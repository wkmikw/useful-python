#coding=utf8
#python 666.py
import os
import sys

#print(os.listdir('\TDDOWNLOAD\[Mikehouse] Emperor'))
tt = os.listdir('\TDDOWNLOAD\dva')
num=1
os.chdir('\TDDOWNLOAD\dva')
for i in tt:
	if num < 10:
		newname = '0000000%s.jpg' % num
	elif num < 100:
		newname = '000000%s.jpg' % num
	else:
		newname = '00000%s.jpg' % num
	os.rename(i, newname)
	num = num + 1
