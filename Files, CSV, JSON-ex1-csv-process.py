# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:49:48 2018

@author: Dimitrios
"""

import csv
def readcsvShort (filename):
    file1 = open(filename)
    reader = csv.reader(file1, delimiter=',')
    print ('reader=',type(reader))
    data = list(reader)
   
    return data


data=readcsvShort('example.csv')
print (data)


#readcsvLong('example.csv')
