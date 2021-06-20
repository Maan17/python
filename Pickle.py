import pickle
data={
    'a':[1,2.5,3,4],
    'b':("character string"),
    'c':{None,True,False}
    }
file=open('data.pickle','wb')
pickle.dump(data,file,pickle.HIGHEST_PROTOCOL)
file.close()
print("data written")

file=open('data.pickle','rb')
print("Data from file:")
data=pickle.load(file)
file.close()
