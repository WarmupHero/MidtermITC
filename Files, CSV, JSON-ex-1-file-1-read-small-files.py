# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:33:40 2019

@author: dimitrv
"""

#open file
inpFile = open ("file1.txt","r")

#Get list of all lines in file
allData = inpFile.read()

#close file
inpFile.close()
