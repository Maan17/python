

class Student:

    def  __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):#overloading add() method
        m1=self.m1 +other.m1
        m2=self.m2 +other.m2
        s3=Student(m1,m2)

        return s3

    def __gt__(self,other):#overloading gt() method
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):#overriding str method to return the value of object which only returns address of object
        return '{} {} '.format(self.m1,self.m2)




s1=Student(58,61)
s2=Student(49,56)

s3=s2+s1

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s1)
