#Function to convert number to string
#Switcher is dictionary data type here
def numbers_to_strings(argument):
  switcher={
    0:"zero",
    1:"one",
    2:"two",
    }

#get() method of dictionary data type returns value of passed argument if it is present in the
#dictionary otherwise second argument will be assigned as default value of passed argument
  return switcher.get(argument,"nothing")

#driver program
if __name__=="__main__":
  argument=int(input("Enter an integer:"))
  print (numbers_to_strings(argument))
