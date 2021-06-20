#working of range() without step

#using range()
lis1=list(range(6))
lis2=list(range(3,6))
lis3=list(range(-6,2))

#initializing list using range,1 parameter(only stop)
print("List generated using 1 parameter:",lis1)

#initializing list using range,2 parameter(only step & stop)
print("\nList generated using 2 parameter:",lis2)

#initializing list using range,2 parameter(only stop & step)
print("\nList generated using 2 parameter:",lis3)

#working of range() with step

#initializing list using range,using step
print("List generated using step:",list(range(3,10,2)))

#initializing list using range,using negative step
print("List generated using negative step:",list(range(10,-5,-3)))

#initializing list using range,using negative step,value constraints fail case
print("List generated using negative step,value constraints fail case:",list(range(10,-5,3)))


#printing a number
for i in range(10):
  print("\n",i,end="")
print()

#using range for iteration
l=[10,20,30,40]
for i in range(len(l)):
  print("\n",l[i],end="")
print()

#performing sum of natural number
sum=0
for i in range(1,10):
  print(i)
  sum=sum+i
print("\nSum of First 10 natural number:",sum)

#incremented with range by 2
for i in range(2,25,1):
  print("\n",i,end=" ")
print()

#decrementing with range by 2
for i in range(25,2,-1):
   print("\n",i,end=" ")
print()
