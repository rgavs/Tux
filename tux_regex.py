#!/bin/python

import re
import datetime
import tux_rss

email = input('Email address:\t').upper()
# This will match \ USERNAME@SITE.SUB.DOMAIN \
regex = re.compile('[A-Z0-9._%+-]+@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}')
matchObj = re.search(regex , email)

if(matchObj != None and matchObj.span()[1] == len(email)):
	print("IT DO WERK")
else:
	print("That's not a proper email address.")

# Automatically generate datetime.date object with current date
form = input('Enter a datetime format if you would like, \t')
if(form != None):
	try:
		dt = datetime.date.__format__(form)
	except ValueError:
		dt = datetime.date.__format__(...)


