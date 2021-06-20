#python program to illustrate list;

#create an empty list
num=[]

#appending data in the list
num.append(21)
num.append(40.5)
num.append(1)
num.append(32)
num.append(89)
print(num)
print("Element at index 0 is:",num[0])
print("Element from 2 index are:",num[2:])
print("Last element is:",num[-1])

names=['maansi','crush','john']

#combining 2 lists
mil=[num,names]
print("Concatenation of 2 lists:",mil)

#inserting element at specific index
num.insert(2,77)
print("Insertion of 77 at index 2:",num)

#removing a specific element
num.remove(40.5)
print("Removing 40.5:",num)

#popping an element
print("Popping element at index 3:",num.pop(3))
#when no index is mentioned last element is popped
print("Popping last element:",num.pop())

#adding more elements in list
num.extend([29,12,14,36])
print("Extending the list:",num)

#minimum number in list
print("Minimum element in list:",min(num))

#maximum number in list
print("Maximum element in list:",max(num))

#sum of all elements in list
print("Sum of all elements in list:",sum(num))

#sorting all the elements in ascending order
num.sort()
print("Ascending order:",num)

#reversing the elements
num.reverse()
print("Reversing the elements in list:",num)

#index of an element
print("Index of 77:",num.index(77))

#input list from user
lst=input("Enter the elements of the list 1:").split()
print("The list elements are:",lst)
print(lst[2])


