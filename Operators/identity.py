#examples of identity operators
a1=int(input("Enter 1st number:"))
a2=int(input("Enter 2nd number:"))
b1=input("Enter 1st String:")
b2=input("Enter 2nd String:")
c1=input("Enter the elements of the list 1:").split()
c2=input("Enter the elements of the list 2:").split()

#using 'is' identity operator
#true when operands are identical
print("a1 is identical to a2:",a1 is a2)
print("b1 is identical to b2:",b1 is b2)
print("c1 is identical to c2:",c1 is c2)

#using 'is not' identity operator
#true when operands are not identical
print("a1 is not identical to a2:",a1 is not a2)
print("b1 is not identical to b2:",b1 is not b2)
print("c1 is not identical to c2:",c1 is not c2)

