#check if a class is subclass of another

class Base(object):
  pass #empty class

class Derived(Base):
  pass #empty class

#driver code
print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d=Derived()
b=Base()

#b is not an instance of derived
print(isinstance(b,Derived))

#but d is an instance of Base
print(isinstance(d,Base))
