#Program to demonstrate conditional operator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("a is equal to b" if a==b else "a is greater than b" if a>b else "b is greater than a")
