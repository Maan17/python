from numpy import *

'''use pycharm'''
#adding a value to each element of array
arr=array([1,2,3,4,5])
arr=arr+5
print(arr)

#adding two different arrays(vectorized operation)
arr1=array([1,2,3,4,5])
arr2=array([5,6,7,8,9])
print(arr1+arr2)

#performing certain operations on array
print(sin(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

#concatenating two arrays
print(concatenate([arr1+arr2]))

#copying array with different address
arr1=array([2,6,8,1,3])
arr2=arr1.view()#gives you shallow copy
print(arr1)
print(arr2)
print(id(arr1),id(arr2))
arr2=arr1.copy()#will give you deep copy

