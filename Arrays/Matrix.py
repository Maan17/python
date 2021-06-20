from numpy import *

'Do in pycharm'
arr1=array([
             [1,2,3,6,2,9],
             [4,5,6,7,5,3]
])

#converting array to matrix
print("The array in Matrix format is:",matrix(arr1))

#converting string to matrix
print("String in matrix format is:",matrix('1 2 3;6 4 5;1 6 7'))

#printing diagonal elements in matrix
m=matrix('1 2 3;6 4 5;1 6 7')
print("The diagonal matrix are:",diagonal(m))

#multiplication of two matrices
m2=matrix('1 2 3;6 8 5;2 6 7')
print("The multiplication of two matrices is:",m*m2)
