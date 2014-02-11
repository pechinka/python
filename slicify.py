#!/usr/bin/python
import string
import re
import math
from datetime import date

#['Booking ID', 'Start Time', 'End Time', 'Hourly Rate', 'Machine Spec', 'Total Hours', 'Total Billed', 'Slicify Commission Paid', 'Total Net Commission']
#['51046', '2/9/2014 6:14:34 PM', '2/9/2014 6:37:01 PM', '$0.01', 'Intel(R) Core(TM) i5 CPU M 520 @ 2.40GHz 3 core / 1536 mb RAM', '1', '$0.01', '$0.01', '$0.00']

f = open("slicifyMyCommission.txt", "r");
f.readline() # skip table header
text = re.split(r'\r\n', f.read())

sumtotalnetcommission = 0.00
sumtotalhours = 0
for line in text:
	linecells = re.split(r'\t', line)
		
	totalnetcommission = string.replace(linecells[8], '$', '')
	sumtotalnetcommission = sumtotalnetcommission + float(totalnetcommission)
		
	totalhours = linecells[5]
	sumtotalhours = sumtotalhours + int(totalhours)	

print 'Hired for: ' + str(sumtotalhours) + ' hours'
print 'Hired Time Commision: $' + str(sumtotalnetcommission)

f = open("slicifyMyAccount.txt", "r");
firstline = f.readline()
connectiontime = string.replace(firstline, 'current accumulated connection time is: ', '')
connectiontime = string.replace(connectiontime, ' hours', '')
bonus = int(connectiontime) / 250 * 5 # $5 bonus for each 250 hours
print 'Uptime bonus: $' + str(bonus)

usage = round((float(sumtotalhours) / float(connectiontime) * 100), 2) 
print 'Hired Time: ' +str(usage) + ' %'

payout = sumtotalnetcommission + bonus
print 'Total Payout: $' + str(payout)
	
f.close()