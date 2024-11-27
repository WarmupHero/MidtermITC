# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:59:44 2018

@author: Dimitrios
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:49:48 2018

@author: Dimitrios
"""

#Create a dictionary, where <keys> are the movie-IDs
# and <values> are the name of the actors that participated in the movie

import csv

#read a CSV file, note that the columns are separated with TABs
def readcsvShort (filename):
    file1 = open(filename, errors='ignore')
    reader = csv.reader(file1, delimiter='\t')
    
    data = list(reader)
    
   
    return data





actors=readcsvShort('movie_actors.dat')

#movieActors is a dictionay with: <key,values>=<movieID, [actor1, actor2, ...]   
movieActors={}
for item in actors:
    if item[0] in movieActors:
        movieActors[item[0]].append(item[2])
    else:
        movieActors[item[0]]=[item[2]]    
        
        
        
#movieActors['65133']
#['Colin Firth',
# 'Hugh Laurie',
# 'Kate Moss',
# 'Miranda Richardson',
# 'Patsy Byrne',
# 'Rik Mayall',
# 'Rowan Atkinson',
# 'Stephen Fry',
# 'Tim McInnerny',
# 'Tony Robinson']

    
