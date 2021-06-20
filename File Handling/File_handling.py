'''#works in pycharm
f=open('MyData','r' ) #opening a file(read command)

print(f.read())#printing a data
print(f.readline())#prints 1st line ,then 2nd line and so on
print(f.readline(4))#prints 4 characters

f1=open('abc','w')#write command
f1.write('something')#writing something in the file abc
f1=open('abc','a')#append command
f1.write('Laptop')#writing something in the file abc

#printing one by one
for data in f:
    print(data)'''

'''file=open('mytxt.txt','w+')
data="Hello how are you\n I am good.\nWhat about you\b"
file.write(data)
file.close()
print('your file is ready')'''

'''file=open('mytxt.txt','r')
for row in file.readlines():
    print(row)'''

#analysing data in a file
file=open('cric.txt','r+')
pid= input("Enter pid")
name=input("Enter name")
score=input("Enter score")
fours=input("Enter six")
six=input("Enter fours")

new_data="\n"+",".join([pid,name,score,fours,six])
file.write(new_data)
file.close()

totalfour=0
totalsix=0
totalhund=0
totalfifty=0
file=open('cric.txt','r')
for row in file.readlines():
    pid,name,score,fours,six=row.split(',')
    totalfour+=int(fours)
    totalsix+=int(six)
    if int(score)>=100:
        print(name)
        totalhund+=1
    if int(score)<100 and int(score)>=50:
        totalfifty+=1
print(totalfifty)        
print(totalhund)
print(totalfour)
print(totalsix)
