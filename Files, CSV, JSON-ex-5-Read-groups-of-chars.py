# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:37:16 2018

@author: Dimitrios
"""

#number of charactes to read
nChars=5
infile = open("test.txt", "r")
while True:
    c = infile.read(nChars)
    if c == '':
        print ("End of file")
        break
    else:
        c = infile.read(nChars)
        print(c)
