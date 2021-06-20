#ANY and ALL operators

li1=[True,True,True,True]
li2=[False,False,False,False]
li3=[True,False,False,True]

print(li1)
print(li2)
print(li3)

#using ANY
print("ANY for list 1:",any(li1))
print("ANY for list 2:",any(li2))
print("ANY for list 3:",any(li3))

#using ALL
print("ALL for list 1:",all(li1))
print("ALL for list 2:",all(li2))
print("ALL for list 3:",all(li3))
