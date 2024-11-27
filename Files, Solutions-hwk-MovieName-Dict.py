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
# and <values> are the names of the actors that participated in the movie

# the create a dictionart, where <keys> are the movie-Names
# and <values> are the names of the actors that participated in that movie

import csv

#read a CSV file, note that the columns are separated with TABs
def readcsvShort (filename):
    file1 = open(filename, errors='ignore')
    reader = csv.reader(file1, delimiter='\t')
    
    data = list(reader)
    
    #delete the header
    del data[0]
    
    return data




# read movies, and movie_actors files
# you need also to understand their contents, so 
# open them with a text editor


# movies.dat
#id 	title	imdbID	 spanishTitle	imdbPictureURL	year	 ...
#1  Tou Story 0114709 Toy story      http://        1995   ...
data=readcsvShort('movies.dat')

# movie_actors.dat
#movieID	actorID	actorName	ranking
#1	annie_potts	Annie Potts	10
actors=readcsvShort('movie_actors.dat')

#moviesDict is a dictionary with: <key,values>=<movieID, movieName>
moviesDict={}
for item in data:
    moviesDict[item[0]]=item[1]

#movieActors is a dictionay with: <key,values>=<movieID, [actor1, actor2, ...]   
movieActors={}
for item in actors:
    if item[0] in movieActors:
        movieActors[item[0]].append(item[2])
    else:
        movieActors[item[0]]=[item[2]]    

#movieActors is a dictionay with: <key, values>=<movieName, [actor1, actor2, ...]
movieNameActors={}
for item in movieActors:
        movieNameActors[moviesDict[item]]=movieActors[item]
    
