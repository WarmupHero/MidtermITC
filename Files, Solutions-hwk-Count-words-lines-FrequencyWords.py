#files basic commands

# count number of lines
# count number of words
# count number of uniq words
# print words and number of appearences


import matplotlib.pyplot as plt
import numpy as np

filename='war-and-peace.txt'
#filename=input (" Please enter the file name ")


fp = open(filename,encoding="utf8")
lineCtr = 0
wordCtr = 0
uniqWords={}
stopWords=['the','he','and','of','his','is','in','that','an','as',
           'who','as','so','on','at','him','we','would','up','as',
           'but','i','it','no','us','to','its','a','with','over','her','she',
           'he','if','you','this','your','i','they','or','not','are','me',
           'it','my','am','was','had','for','when','by','be','from','which',
           'all','into','their','how','what','these']

#stopWords=[]


for line in fp:
    numOfWordsinLine = len(line.split())
    wordCtr = wordCtr + numOfWordsinLine 	
 
    for word in line.split(): 
      word=word.lower()
      if word.lower() in uniqWords:
           uniqWords[word]=uniqWords[word]+1
      else:
          if word not in stopWords:
              uniqWords[word]=1

    lineCtr = lineCtr + 1

print ("number of lines = ", lineCtr)
print ("number of words = ", wordCtr)
print ('number of non stop words=',len(uniqWords))




#change: 
#    reverse to false to see the difference
#    change key to uniqWords.get 
#    uniqWords.get:  gets the values
for w in sorted(uniqWords, key=uniqWords.get, reverse=False):
      print (w, uniqWords[w])



#let us do some plots
plt.title ("Words in reverse order of frequency")
plt.close(1)
plt.close(2)
plt.close(3)

plt.figure(1)
plt.title ('Word frequency ')
plt.plot(sorted(uniqWords.values(), reverse=True),'.')
plt.ylabel(" Frequencies")
plt.xlabel(" words ")



plt.figure(2)
plt.title ('Word frequency-log scale')
plt.ylabel(" Frequencies")
plt.plot(np.log10(sorted(uniqWords.values(), reverse=True)),'.')


plt.figure(3)
plt.title('Frequencies of Words: boxplot')
plt.boxplot(uniqWords.values())

fp.close()


