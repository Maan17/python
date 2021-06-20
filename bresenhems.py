import math
import numpy
import matplotlib.pyplot as plt
x1,x2=[int(x) for x in input("Enter x1 and x2: ").split()]
print("x1 is {} and x2 is {}".format(x1,x2))
y1,y2=[int(x) for x in input("Enter y1 and y2: ").split()]
print("y1 is {} and y2 is {}".format(y1,y2))
dx=abs(x2-x1)
dy=abs(y2-y1)
if dx>dy:
    l=dx
else:
    l=dy
dx=(x2-x1)/l
dy=(y2-y1)/l
x=round(x1+0.5*dx)
y=round(y1+0.5*dy)
i=1
myarray=[]
while(i<=l):
    myarray=numpy.array([x,y])
    x=x+dx
    y=y+dx
    i=i+1
plt.plot(myarray)
plt.show()

