# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:37:16 2018

@author: Dimitrios
"""
# Read the file in one command-only: All data go to variable 'a'\
#it might not work with big data
try:
    infile = open ("war-and-peace.txt", "r",  errors='ignore')
    
    a=infile.read()
    print(a)

    wordList=a.split(' ')

    freqWords=dict()

    for word in wordList:
        if word in freqWords:
            freqWords[word]+=1
        else:
            freqWords[word]=1
    
except FileNotFoundError:
    print ("There is no file named . Please try again")


