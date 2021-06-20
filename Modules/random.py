#import built-in module random
import random

#print random integer between 0 &5
print (random.randint(0,5))

#print random floating point number
print (random.random())

#random number between 0 & 100
print (random.random()*100)

list=['M','100','maths','aei']

#using choice() to genereate a random number fom the list
print (random.choice(list))

#using randrange() to generate in range from 20 to 50.
#The last parameter 3 is step size to skip 3 nos. while selecting
print("A random number from range is:",random.randrange(20,30,3))

#using random() to generate a float random number
#between 0 and 1
print("A random no. b/w 0 &1 is:",random.random())

#using seed() to seed a random number
random.seed(5)

#printing mapped random number with 5
print("The mapped random number with 5 is:",random.random())

#printing list before shuffling
print("List before shuffling:",list)

#using shuffle() to shuffle the list
random.shuffle(list)

#printing list after shuffling
print("List after shuffling:",list)

#using uniform() to generate random floating number in range
#prints number b/w 5 & 10
print("The random floating point number between 5 & 10 is:",random.uniform(5,10))



