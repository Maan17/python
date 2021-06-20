#functions

def hello():
    print("Hello")
    print("Hello again")

#calling functions
hello()
hello()
    
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(5,4)
print(result1,result2)

def update(x):

    
    x=8
    print("x ",x)

a=10
update(a)
print("a ",a)
