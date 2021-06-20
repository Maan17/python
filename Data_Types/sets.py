#examples on set
set1=set(["Geeks","For",1,2,"Geeks",])
print(len(set1))
print(set1)

#adding element to set
set1.add(8)
set1.add(9)
set1.add(9)
print("Set after addition of 3 elements:",set1)

#removing elements
#using remove() method
set1.remove("Geeks")
set1.remove(1)
print("Set after removal of two elements:",set1)
#using pop() method
set1.pop()
print("Set after popping an element:",set1)
#using clear() method
print("Set after clearing all elements:",set1)

#frozen set
fset1=frozenset("String")
print("The frozen set is:",fset1)

#union of set
people={"Jay","Irdish","Archil",1,3}
vampires={"Karan","Arjun",1,3}
print("Union using union() method:",people.union(vampires))
print("Union using | operator:",people|vampires)

#intersection
print("Intersection using intersection() method:",people.intersection(vampires))
print("Intersection using & operator:",people&vampires)

#difference
print("Difference by difference method():",people.difference(vampires))
print("Difference by - operator:",people-vampires)
