from array import *

#blank array
arr=array('i',[])

#defining integer array
vals=array('i' ,[5,9,8,4,2])

#defining character array
vals=array('u',['a','e','i','o'])
 
#when you don't know the type
newArr=array(vals.typecode,(a for a in vals))

#printing address of array
print(vals.buffer_info)

#printing type
print(vals.typecode)

#printing value at a particular index
print(vals[0])

#input from user
n=int(input("Enter the length of the array:"))
for i in range(n):
  x=int(input("Enter the next element of the array:"))
  arr.append(x)

print(arr)

#printing the index number of an arr
#manually
val=int(input("Enter the value for search"))
k=0
for e in arr:
  if e==val:
    print(k)
    break
  k+=1
#using function  
print(arr.index(val))  

