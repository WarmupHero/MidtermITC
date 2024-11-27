# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:37:16 2018

@author: Dimitrios

Copy input to output
"""

lines=0
infile  = open("file1.txt", "r")
outfile = open('test.txt','w')
for c in infile:
    outfile.write(c)
    lines+=1
    
    
outfile.close()
infile.close()
    
print ('lines read=',lines)