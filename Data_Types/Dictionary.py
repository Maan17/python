#examples in dictionary

# an empty dictionary
Dict={}
print("Empty Dictionary:")
print(Dict)

#with Integer keys
Dict={1:'Geeks',2:'For',3:'Geeks'}
print("Dictionary with the use of Integer keys:",Dict)

#adding elements one at a time
Dict[4]='Maan'
Dict[6]=1
print("Dictionary after adding 3 elements:",Dict)

#updating existing key's value
Dict[2]='Welcome'
print("Updated key vakue:",Dict)

#accessing a element using key
print("Acessing a element using key:",Dict[6])

#accessing an element using get() method
print("Acessing an element using get:",Dict.get(3))

#Deleting a key value
del Dict[6]
print("Deleting a specific key:",Dict)

#using pop()
Dict.pop(2)
print("Popping specific element:",print(Dict))

#using popitem()
Dict.popitem()
print("Pops first element:",print(Dict))

#Deleting entire Dictionary
Dict.clear()
print("Deleting entire dictionary:")

#initializing dictionary
dic={'Name':'Nandini','Age':19}

#using str() to display dic as string
print("The constituents of dictionary as strings are:",str(dic))

#using str() to display dic as list
print("The constituent of dictionary as list are:",dic.items())

#using len() to display dic size
print("The size of dic is:",len(dic))

#using type() to display data type
print("The data type of dic is:",type(dic))

dic3={}

#using copy() to make shallow copy of dictionary
dic3=dic.copy()

#printing new dictionary
print("The new copied dictionary is:",dic3.items())

dic1={'Name':'Nandini','Age':19}
dic2={'ID':2541997}
sequ=('Name','Age','ID')

#using update to add dic2 values in dic1
dic1.update(dic2)

#printing updated dictionary values
print("The updated dictionary is:",str(dic1))

#using fromkeys() to transform sequence into dictionary
dict=dict.fromkeys(sequ,5)

#printing new dictionary values
print("The new dictionary values are:",str(dict))

#using get() to print a key value
print("The value associated with ID is:")
print(dict.get('ID','Not Present'))

#printing dictionary values
print("The dictionary values are:",str(dict))

#using setdefault() to print a key value
print("The value associated with Age is:",dict.setdefault('ID','No ID'))

#printing dictionary values
print("The dictionary values are:",str(dict))
Dict={'sid':[101,102,103,104], 'result':['pass','fail','pass','fail'],'name':['H','M','S','R']}
a=input("Enter the id")
a=Dict['a'].index(sid)
print(Dict['result'][a])
