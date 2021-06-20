file=open("mytxt.txt","r")
print(file.read())
print(file.tell())
#move the cursor to a specific position
file.seek(2,0)
print(file.readline())
print(file.tell())
