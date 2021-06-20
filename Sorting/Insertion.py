from array import *
size=int(input("Enter the size of the array:"))
arr=array('i',[])
for i in range(size):
    arr.append(int(input("Enter the next element of the array:")))
key=0
for j in range(1,size):
    key=arr[j]
    i=j-1
    while(i>=0 and arr[i]>key):
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1]=key
print(arr)
