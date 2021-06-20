#sorting a list without creating another list
#use of sort()
def Sorting(lst):
  lst.sort(key=len)
  return lst

#sorting a list by creating another list
#use of sorted()
def Sorting2(lst):
  lst2=sorted(lst)
  return lst2

lst=["rohan","amy","sapna","muhammad","aakash","raunak","chinmoy"]
print(Sorting(lst))
print(Sorting2(lst))
