#return double of n
def addition(n):
    return n+n

#we double all numbers using map()
numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))

#double all numbers using map and lambda
result=map(lambda x:x+x,numbers)
print(list(result))

#adding two list using map and lambda
numbers1=[1,2,5]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))

#list of strings
l=['sat','bat','cat','mat']
#map() can listify the list of strings individually
test=list(map(list,l))
print(test)
print(test[0][1])
