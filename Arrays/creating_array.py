from numpy import *

'''run in pycharm'''
# ways of creating array
# 1.array()
arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)

#2.linspace()
arr=linspace(0,15,20)
print(arr)

#3.arange
arr=arange(1,15,2)
print(arr)

#4.logspace
arr=logspace(1,40,5)
print(arr)

#5.zeroes()
arr=zeros(5)
print(arr)

#6.ones()
arr=ones(5,int)
print(arr)
