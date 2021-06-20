file=open("mytxt.txt","r")
word_list=file.read().split()
word_length=[]
for i in word_list:
    word_length.append(len(i))
print(word_length)
print(len(word_list))
wordcount=dict()
for word in word_length:
    if word in wordcount:
        wordcount[word]+=1
    else:
        wordcount[word]=1
print(wordcount)        
