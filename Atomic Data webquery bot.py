# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:08:02 2014

@author: choog_000
"""

from bs4 import BeautifulSoup as BS
import urllib2
import re

##opening and reading the element list file##
element_file = "C:\\Users\\choog_000\\Documents\\Socrata\\NIST\\basic_atomic_spectroscopic_lookup_dictionary.txt"
element_file_text = open(element_file, "r")
element_file_read = element_file_text.read()
elements_lowercase = element_file_read.lower()
element_list = re.split('\W+',elements_lowercase)

##create output file to pipe results to##
myFile = open("C:\\Users\\choog_000\\Documents\\Socrata\\NIST\\output.txt",'w')

##repeatedly query changing URL, pull down data, and write data to output file##
for element in element_list:
    data = urllib2.urlopen("http://www.physics.nist.gov/PhysRefData/Handbook/Tables/" + element + "table1_a.htm")
    readData = data.read()
    print readData 

Element_name = ""
Atomic_number = ""
Atomic_weight = ""
Isotope = ""
Mass = ""
Abundance = ""
Spin = ""
Mag_moment = ""

    
 myFile.write(readData)
    myFile.write('\n')
    
##unit test with one URL request##    
    data = urllib2.urlopen("http://www.physics.nist.gov/PhysRefData/Handbook/Tables/actiniumtable1.htm")
    readData = data.read()
    print readData