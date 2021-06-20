#simple for loop
num=int(input("Enter the number of times:"))
for i in range(num):
    print(i)

#iterating over list
print("\nList iteration:")
l=["geeks","for","geeks"]
for i in l:
    print(i)

#iterating over tuple
print("\nTuple iteration:")
t=("geeks","for","geeks")
for i in t:
    print(i)

#iterating over a string
print("\nString iteration:")
s="Geeks"
for i in s:
    print (i)

#iterating over dictionary
print("\nDictionary iteration:")
d={'xyz':123,'abc':345}
for i in d:
    print("%s %d"%(i,d[i]))

#iterating by index
print("\nIterating by index:")
for index in range(len(l)):
    print(l[index])

#combining else with for
print("\nWith else:")
for i in range(len(l)):
    print(l[i])
else:
    print("Inside else block")

#nested for
print("\nNested:")
for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()

#continue in loop
print("\nLetter excluding e and s:")
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print("Current letter:",letter)

#break in loop
print()
for letter in 'geeksfor geeks':
    #break the loop as soon it sees e or s
    if letter=='e' or letter =='s':
        break
print("Current letter:",letter)

#pass in loop
print()
for letter in 'geeksforgeeks':
        pass
print("Last letter:",letter)

#printing the list in reverse order
list=input("Enter the list:").split()
print("List in reverse order is:")
for i in range(len(list),0):
    print(list[i])
