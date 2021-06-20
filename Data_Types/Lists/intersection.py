#simple way
def intersection1(lst1,lst2):
  lst3=[value for value in lst1 if value in lst2]
  return lst3

#use set()
def intersection2(lst1,lst2):
  return list(set(lst1) & set(lst2))

#using set() and intersection()        
def intersection3(lst1,lst2):
  return set(lst1).intersection(lst2)

#using hybrid method
def intersection4(lst1,lst2):
  temp=set(lst2)
  lst3=[value for value in lst1 if value in temp]
  return lst3

#using filter()
def intersection(lst1,lst2):
  lst3=[list(filter(lambda x:x in lst1,sublist))for sublist in lst2]
  return lst3

#driver code
lst1=[4,9,1,17,11,26,28,54,69]
lst2=[9,9,74,21,45,11,63,28,26]
print("Simple method: ",intersection1(lst1,lst2))
print("Using Set: ",intersection2(lst1,lst2))
print("Using Set and Intersection: ",intersection3(lst1,lst2))
print("Using Hybrid: ",intersection4(lst1,lst2))       
        
