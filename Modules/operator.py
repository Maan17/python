#import operator to handle operator operations
import operator

#using iadd() to add and assign values
x=operator.iadd(2,3)
print("The value after adding and assigning: ",x)

#initializing values
y="geeks"

z="forgeeks"

#using iconcat() to concat the sequences
y=operator.iconcat(y,z)
print("The string after concatenation: ",x)

#using isub() to subtract and assign value
a=operator.isub(2,3);
print("The value after subtracting and assigning:",a)

#using imul() to multiply and assign value
b=operator.imul(2,3)
print("The value after multiplying and assigning:",b)

#using itruediv() to divide and assign value
c=operator.itruediv(10,5)
print("The value after assigning and dividing:",c)

#using imod() to modulus and assign value
d=operator.imod(10,6)
print("The value after modulus and assigning:",d)

#using ixor() to exclusive or and assign value
e=operator.ixor(10,5)
print("The value after xoring and assigning:",e)

#using ipow() to exponentiate and assign value
f=operator.ipow(5,4)
print("The value after exponentiating and assigning:",f)

#using iand() to and,and assign value
g=operator.iand(5,4)
print("The value after bitwise and,and assigning:",g)

#using ior() to or,and assign value
h=operator.ior(10,5)
print("The value after bitwise or,and assigning:",h)

#using ilshift() to bitwise left shift and assign value
i=operator.ilshift(8,2)
print("The value after bitwise left shift and assigning:",i)

#using irshift() to bitwise right shift and assign value
j=operator.irshift(8,2)
print("The value after bitwise right shift and assigning:",j)


