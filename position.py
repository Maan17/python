file=open("mytxt.txt","r")
import re
from re import *
print(file.read())
print(file.tell())
#move the cursor to a specific position
file.seek(2,0)
print(file.readline())
print(file.tell())

#counting the number of occurences of  a word 
c=0
word_list=file.read().split()
print(len(word_list))
wordcount=dict()
for word in word_list:
    if word in wordcount:
        wordcount[word]+=1
    else:
        wordcount[word]=1
print(wordcount)        
    


