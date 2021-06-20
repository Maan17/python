class A:#Super Class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

#single level inheritance
class B(A):#subclass
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class D:
    def feature6(self):
        print("Feature 6 working")

#multilevel inheritance
class C(B):
    def feature5(self):
        print("Feature 5 is working")

#multiple inheritance
class E(A,D):
    def feature7(self):
        print("Feature 7 is working")

