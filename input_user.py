#Getting input from user
##name=input("Enter your name ")
##
###user entered name
##print("Hello",name)
##
###typecasting input to integer
##num1=int(input("Enter 1st number:"))
##num2=int(input("Enter 2nd integer:"))
##print("The sum is:",num1+num2)
##
###typecasting input to float
##num1=float(input("Enter 1st Float number:"))
##num2=float(input("Enter 2nd Foat number:"))
##print("The sum is:",num1+num2)
##
###typecasting input to string
##string=str(input("Enter a String:"))
##print(string)


# number of elements
n = int(input("Enter number of elements : "))
  
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
  
print("\nList is - ", a)
