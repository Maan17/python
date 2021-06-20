#filter() with lambda
li=[5,7,22,97,54,62,77,23,73,61]
final_list=list(filter(lambda x:(x%2!=0),li))
print(final_list)

#map() with lambda
final_list=list(map(lambda x:x*2,li))
print(final_list)

#lambda() to get sum of a list
from functools import reduce
li=[5,8,10,20,50,100]
sum=reduce((lambda x,y:x+y),li)
print(sum)
