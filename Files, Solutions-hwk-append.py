# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:37:16 2018

@author: Dimitrios

Copy input to output
"""

# append the contexts of the first file to the second file

lines=0
infile  = open("file1.txt", "r")
outfile = open('file2.txt','a')
for c in infile:
    outfile.write(c)
    
    
outfile.close()
infile.close()
    
print ('lines read=',lines)