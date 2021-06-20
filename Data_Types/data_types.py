#type of data

#NUMERIC:
#float type
num=3.4
print("3.4 is float type:",type(num))

#int type
num=5
print("5 is int type:",type(num))

#complex type
num=6+9j
print("6+9j is complex type",type(num))

#bool type
num=9>10
print(9>10,"is boolean type:",type(num))
#integer value of bool True and bool False
print("Integer value of True is ",int(True)," and False is ",int(False))

#typecasting

a=5.6

#conversion to int
b=int(a)
print("a is ",type(a)," and b is ",type(b))

#conversion to float
k=float(b)
print("b is ",type(b)," and k is ",type(k))

#conversion to complex
c=complex(b,k)
print("c is type",type(c))

#LIST
lst=[25,36,45,12]
print("lst is type:",type(lst))

#SET
s={25,36,45,15,12,25}
print("s is type",type(s))

#TUPLE
t=(25,36,4,57,12)
print("t is type:",type(t))

#STRING
str='maansi'
print("str is typr:",type(str))

#RANGE
range(10)
print("Elements present in range 10:",list(range(10)))

#DICTIONARY
d={'maansi':'samsung','rahul':'Iphone','kiran':'Oneplus'}
print("The elements of dictionary are:",d)

#getting key 
print("The keys are",d.keys())

#getting values
print("The values are",d.values())

#getting specific values using key
print("Value associated with key Rahul is:",d['rahul'])
print("Value associated with key Kiran is:",d.get('kiran'))
                                              



