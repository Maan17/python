#demonstrate the working of zip

#two seperate lists
cars=["Aston","Audi","McLaren"]
accessories=["GPS","Car Repair Kit","Dolby sound kit"]

#combining lists and printing
for c,a in zip(cars,accessories):
  print("Car:  %s,    Accessory required:  %s"%(c,a))

#demonstrate unzip(reverse of zip) using * with zip function

#unzip lists
l1,l2=zip(*[('Aston','GPS'),('Audi','Car Repair'),('McLaren','Dolby sound kit')])

#printing unzipped list
print(l1)
print(l2)
