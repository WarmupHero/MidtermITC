# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:37:16 2018

@author: Dimitrios
"""


#Read input file, line by line
lines=0
chars=0
infile = open("file3.txt", "r")
for c in infile:
    print (c,end='')

    lines+=1
    
    
    
print ('lines read=',lines)