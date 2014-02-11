#!/usr/bin/env python
"""slicify.py: Show spend time and payouts."""
__author__      = "Petr Pohl"
__copyright__   = "Copyright 2014"
import re

def slicify():
    """Show spend time and payouts."""
    fmc = open("slicifyMyCommission.txt", "r")
    fmc.readline() # skip table header
    text = re.split(r'\r\n', fmc.read())
    
    sumtotalcommission = 0.00
    sumtotalhours = 0
    for line in text:
        linecells = re.split(r'\t', line)
    
        totalcommission = linecells[8].replace('$', '')
        sumtotalcommission = sumtotalcommission + float(totalcommission)
    
        totalhours = linecells[5]
        sumtotalhours = sumtotalhours + int(totalhours)    
    
    print 'Hired for: ' + str(sumtotalhours) + ' hours'
    print 'Hired Time Commision: $' + str(sumtotalcommission)
    
    fma = open("slicifyMyAccount.txt", "r")
    firstline = fma.readline()
    connectiontime = firstline.replace('accumulated connection time is: ', '')
    connectiontime = connectiontime.replace(' hours', '')
    bonus = int(connectiontime) / 250 * 5 # $5 bonus for each 250 hours
    print 'Uptime bonus: $' + str(bonus)
    
    usage = round((float(sumtotalhours) / float(connectiontime) * 100), 2) 
    print 'Hired Time: ' +str(usage) + ' %'
    
    payout = sumtotalcommission + bonus
    print 'Total Payout: $' + str(payout)
    
    fmc.close()
    fma.close()
    
    return 0
    
slicify()

# vim:foldmethod=marker:ts=4:sw=4:noexpandtab