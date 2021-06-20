def add(a,b):#formal arguments
    c=a+b
    print(c)
add(5,6)#actual arguments

#position argument
def person(name,age):
    print("Passing position arguments:",name,end=' ')
    print(age)
person('Maansi',20)

#keyword argument
def person(name,age):
    print("Passing keyword arguments:",name,end=' ')
    print(age)
person(age='20',name='maansi')

#default argument
def person(name,age):
    print("Passing default argument:",age,end=' ')
    print(name)
person(age='20',name='maansi')

#variable length
def add(*b):
    print("passing variable length argument:",sum(b))
add(5,1,1,1)


#keyword variable length arguments
def person(name, **data):
    print("Passing keyword variable length argument",name)
    for i,j in data.items():
        print(i,j)


person('Maansi',age=20,city='Varanasi',mob=8933062633)    
