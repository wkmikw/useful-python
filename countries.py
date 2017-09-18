#coding=utf-8
#python countries.py

from pygal.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.key()):
	print(country_code, COUNTRIES[country_code])
