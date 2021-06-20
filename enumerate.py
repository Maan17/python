#accessing items using enumerate()
cars=["Aston","Audi","McLaren"]
for i,x in enumerate(cars):
  print(i,x)

#use of start in enumerate
print("\nSetting start to 1:")  
for i,x in enumerate(cars,start=1):
  print(i,x)

#Two seperate lists
cars=["Aston","Audi","McLaren"]
accessories=["GPS kit","Car repair-tool kit"]

#single dictionary stores prices of cars and it's accessories
#1st 3 items store prices of cars and next 2 prices of dictionary
prices={1:"570000$",2:"68000$",3:"450000$",4:"8900$",5:"4500$"}

#printing prices of cars
for i,c in enumerate(cars,start=1):
  print("Cars:  %s     Price: %s"%(c,prices[i]))

#printing prices of accessories
for i,a in enumerate(accessories,start=1):
  print("Accessories: %s    Price: %s"%(a,prices[i+len(cars)]))
