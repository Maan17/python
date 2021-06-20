#python program to show that the variables with a value assigned in class declaration,
#are classe variables and variables inside method and constructors are instance variables

#class for Computer Science Student
class CSStudent:

  #class variable
  stream='cse'

  #the init method or constructor
  def __init__(self,name,roll):
    #instance variable
    self.roll=roll
    self.name=name

#objects of CSStudent class
a=CSStudent('Geek',1)
b=CSStudent('Nerd',2)

print(a.stream) #print "cse"
print(b.stream) #print "cse"
print(a.name)   #print"Geek"
print(b.name)   #print "Nerd"
print(a.roll)       #print "1"
print(b.roll)       #print"2"

#class variables can be accessed using class name also
print(CSStudent.stream)#prints "cse"
