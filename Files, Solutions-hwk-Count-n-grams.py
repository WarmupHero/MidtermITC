#count number & frequency of n-grams
#an n-gram is a combination of two letters

import matplotlib.pyplot as plt

filename='war-and-peace.txt'
#filename=input (" Please enter the file name ")


fp = open(filename,"r",encoding="utf8")
allData = fp.read()

fp.close()

# the next is a dictionary of n-grams. eg. 
# key 'wy, value 40,
uniqGrams=dict()

n=2  #N-GRAM,  set it to the size of n-gram
length = len (allData)
for i in range(0, length-n+1):
  #  print(allData[i:i+n])    
    if allData[i:i+n].lower() in uniqGrams:    
        uniqGrams[allData[i:i+n].lower()]=uniqGrams[allData[i:i+n].lower()]+1
    else:
        uniqGrams[allData[i:i+n].lower()]=1
    




#print uniq-grams in reverse order

# The sorted() sorts an iterable, i.e. keys of the uniqGrams dictionary.
# The "key" specifies a function to be called on each element before making comparisons for sorting
# By using uniqGrams.get, the function retrieves the value associated with each key in uniqGrams.
# sorted(): sorts the keys based on their corresponding values in uniqGrams. 

for w in sorted(uniqGrams, key= uniqGrams.get, reverse=False):
      print (w, uniqGrams[w])


print ('Number of Unique n-grams',len(uniqGrams.keys()))


plt.title ("Words in reverse order of frequency")

plt.close(1)
plt.close(2)

plt.figure(1)
plt.plot(sorted(uniqGrams.values(), reverse=True),'.')
plt.ylabel(" Frequncies")
plt.xlabel(" Gram")

plt.figure(2)
plt.title('Frequencies of Grams: boxplot')
plt.boxplot(sorted(uniqGrams.values()))

