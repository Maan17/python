class MyClass:

  #hidden member of MyClass
  __hiddenVariable=0

  #a member method that changes __hiddenVariable
  def add(self,increment):
    self.__hiddenVariable+=increment
    print(self.__hiddenVariable)

#driver code
myObject=MyClass()
myObject.add(2)
myObject.add(5)

#trick to access hidden member
print(myObject._MyClass__hiddenVariable)
