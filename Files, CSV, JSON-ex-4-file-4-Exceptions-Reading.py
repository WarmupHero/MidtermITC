# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:47:44 2018

@author: Dimitrios
"""

try:
    infile = open ("file3s.txt", "r")
    allWords=[]
    for word in infile.read().split():
        print (word)
        allWords.append(word)
        
# handle the case where the file does not exist        
except FileNotFoundError:
    print ("There is no file named ..... Please try again")

# handle other input / output errors
except IOError:
    print ("Error during reading")

except Exception as e:
    print ("Another exception"+e)
    
    
# code that runs always    
finally:
    print ("Ending file reading process")
    



