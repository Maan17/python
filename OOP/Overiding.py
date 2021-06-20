#method overiding
class Parent:
    def getbike(self):
        print("I have ct100")

class Child(Parent):
    def myinfo(self):
        print("I am new born")
    def getbike(self):
        print("I have BMW")   

c=Child()
c.getbike()
    
#child class inheriting parent class as well as it's method
class Parent:
    def getbike(self):
        print("I have ct100")

class Child(Parent):
    def myinfo(self):
        print("I am new born")
    def getbike(self):
        super().getbike()
        print("I have BMW")   

c=Child()
c.getbike()
    
