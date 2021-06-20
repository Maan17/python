#maintained repitition
def Union1(lst1,lst2):
  final_list=lst1+lst2
  return final_list

#maintained repitition and order
def Union2(lst1,lst2):
  final_list=sorted(lst1+lst2)
  return final_list

#without reptition
def Union3(lst1,lst2):
  final_list=list(set(lst1)|set(lst2))
  return final_list

#union of three lists
def Union4(lst1,lst2,lst3):
  final_list=list(set().union(lst1,lst2,lst3))
  return final_list

#driver code
lst1=[23,15,2,14,14,16,20,52]
lst2=[2,48,15,12,26,32,47,54]
lst3=[4,78,5,6,9,25,64,32,59]
print("Maintained repitition: ",Union1(lst1,lst2))
print("Maintained repitition and order: ",Union2(lst1,lst2))
print("Without repitition: ",Union3(lst1,lst2))
print("Union of three lists",Union4(lst1,lst2,lst3))

