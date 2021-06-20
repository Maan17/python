#defining constructor
def __init(self):
    print("Constructor called")

#defining methods
def show(self):
    print("Hello from show")

#defining static method
@staticmethod    
def display():
    print("This is static in python")

#destructor
def __del__(self):
    class_name=self.__class__.__name__
    print(class_name,"destroyed")

class A:
    def __init__(self):
        print("Default const of A")
    def show(self):
        print("I am from show of a")
    @staticmethod    
    def disp():
        print("I am from disp of a ")
A.disp()
a=A()
a.show()
