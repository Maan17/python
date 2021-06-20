#examples on tuples

#creating a tuple
tuple1=(5,'welcome',45,7,'here')
print("Tuple1 is:",tuple1)
tuple2=(1,2,3,4)
print("Tuple2 is:",tuple2)
tuple=input("Enter the tuple:").split()
print(tuple)


#concatenation of tuples
tuple3=tuple1+tuple2
print("Tuples after concatenation:",tuple3)

#slicing of tuple
#removing first element
print("Tuple after removing first element:",tuple1[1:])
#reversing the tuple
print("Reversed tuple:",tuple1[::-1])
#printing elements of a range
print("Printing elements between 4-9",tuple1[4:9])

#deleting a tuple
del tuple1
print("Error after deletion of tuple1:")
print(tuple1)

