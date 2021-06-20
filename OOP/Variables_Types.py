class Car:

    wheels=4#class variables

    def __init__(self):
        #instance variables
        self.mil=10
        self.com='BMW'



c1=Car()
c2=Car()

c1.mil=8

Car.wheels=5

print(c1.com,c1.mil)
print(c2.com,c2.mil)
