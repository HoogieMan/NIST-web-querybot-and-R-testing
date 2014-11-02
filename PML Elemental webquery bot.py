# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:08:02 2014

@author: choog_000
"""
import urllib2
import re
from bs4 import BeautifulSoup

numSet = range(1,119)
Element_name = []
Element_number = []
Atomic_weight = []
Ionization_energy = []
Ground_state_level = []
Ground_state_configuration = []

##repeatedly query the changing URL, pull down data, and perform regex matching to only store core words##
for num in numSet:
    data = urllib2.urlopen("http://physics.nist.gov/cgi-bin/Elements/elInfo.pl?element=" + str(num) + "&context=text")
    readData = data.read()
    soup = BeautifulSoup(readData)
    soupText = soup.get_text()
    
    match1 = re.search(r'retrieve data on \w*\b', soupText)
    if match1:
        Element_name.append(match1.group())
    else:
        print 'nothing1'
    
    match2 = re.search(r'Index: \w*\b', soupText)
    if match2:
        Element_number.append(match2.group())
    else:
        print 'nothing2'
    
    match3 = re.search(r'Atomic Weight: \W\w*\W', soupText)
    if match3:
        Atomic_weight.append(match3.group())
    else:
        print 'nothing3'
        
    match4 = re.search(r'Ionization Energy: .*\eV', soupText)
    if match4:
        Ionization_energy.append(match4.group())
    else:
        print 'nothing4'
    
    match5 = re.search(r'Ground-state Level: .*\n', soupText)
    if match5:
        Ground_state_level.append(match5.group())
    else:
        print 'nothing5'
        
    match6 = re.search(r'Ground-state Configuration: .*\n', soupText)
    if match6:
        Ground_state_configuration.append(match6.group())
    else:
        print 'nothing6'    

print Element_name
print Element_number
print Atomic_weight
print Ionization_energy
print Ground_state_level
print Ground_state_configuration

#write out each list, with a newline character after it
##create output file, then write each list out to mimic a CSV file##
myFile = open("C:\\Users\\choog_000\\Documents\\Socrata\\NIST\\output.txt",'w')
myFile.write(Element_name)
myFile.write('\n')
myFile.write(Element_number)
myFile.write('\n')
myFile.write(Atomic_weight)
myFile.write('\n')
myFile.write(Ionization_energy)
myFile.write('\n')
myFile.write(Ground_state_level)
myFile.write('\n')
myFile.write(Ground_state_configuration)
myFile.write('\n')

###unit test with one URL request##    
#data = urllib2.urlopen("http://physics.nist.gov/cgi-bin/Elements/elInfo.pl?element=116&context=text")
#readData = data.read()
#soup = BeautifulSoup(readData)
#soupText = soup.get_text()
#print soupText
#match6 = re.search(r'Ground-state Configuration: .*\n', soupText)
#if match6:
#    Ground_state_configuration.append(match6.group())
#    print Ground_state_configuration
#else:
#    print 'nothing'