class A:
    a=2
    def show(self):
        self.b=2
        print("I am from A",a)
    def disp(self):
        a=self.a+1
        self.b=self.b+1
        print(a,self.b)
    def disp2(self):
        a=self.a-1
        self.b=self.b-1
        print(a,self.b)
a=A()
a1=A()
a.show()
a.disp()
a1.show()
a1.disp2()
