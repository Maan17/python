from numpy import *

'Do in pycharm'
arr1=array([
               [1,2,3],
               [4,5,6]
])
print(arr1)

#printing the type of array
print("The type of array is:",arr1.dtype)

#printing the dimension of the array
print("The number of dimensions are:",arr1.ndim)

#printing the number of rows and column
print("The no. of rows and columns are",arr1.shape)

#printing the size of the array
print("The size of entire block is:",arr1.size)

arr1=array([
             [1,2,3,6,2,9],
             [4,5,6,7,5,3]
])
#converting 2D array to 1D array
arr2=arr1.flatten()
print("The 1D array from 2D is:",arr2)

#converting 1D array to 2D
arr3=arr2.reshape(3,4)
print("The 2D array from 1D is:",arr3)

#converting 1D array to 3D
arr3=arr2.reshape(2,2,3)
print("The 3D array from 1D is:",arr3)
