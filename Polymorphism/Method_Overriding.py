class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):#overriding show() method of A
        print("In B show")





a1=B()
a1.show()
