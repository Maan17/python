from string import Template

#FORMATING OF STRINGS USING {}

print("Formatting using {}")
#default order
String1="{} {} {}".format('Geeks','For','Life')
print("\nPrint strings in default order:",String1)

#positional formatting
String1="{1} {0} {2}".format('Geeks','For','Life')
print("Print strings in positional order:",String1)

#keyword formatting
String1="{l} {f} {g}".format(g='Geeks',f='For',l='Life')
print("Print strings in order of keywords:",String1)

#formatting of integers
String1="{0:b}".format(16)
print("Binary representation of 16 is:",String1)

#formatting of floats
String1="{0:e}".format(165.6458)
print("Exponent representation of 165.6458 is:",String1)

#Rounding off Integers
String1="{0:.2f}".format(1/6)
print("one-sixth is:",String1)

#string alignment
String1="|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks')
print("Left,center and right alignment with Formatting:",String1 )
  
#FORMATING OF STRINGS USING %

print("Formatting using %")
variable='15'
string="Variable as raw data=%s"%(variable)
print(string)

#printing as raw data
print("Variable as raw data=%r"%(variable))

#convert the variable to integer
#and perform check other formatting options

variable=int(variable)#without this the below statement will give error

string="Variable as integer=%d"%(variable)
print("\n",string)
print("Variable as float=%f"%(variable))

#printing any string or character after a mark
print("Variable as printing with special character=%cmaansi"%(variable))
print("Variable as hexadecimal=%x"%(variable))
print("Variable as octal=%o"%(variable))

#FORMATTING OF STRINGS USING TEMPLATE

print("Formatting using template")
#create template that has placeholder value for x
t=Template('\nx is $x')
#substitute value of x in above template
print(t.substitute({'x':1}))

#list student stores the name and marks of 3 students
Student=[('Ram',90),('Ankit',78),('Bob',92)]
#creating the basic structure to print the name and marks of student
t=Template('Hi $name,you have got $marks marks')

for i in Student:
  print(t.substitute(name=i[0],marks=i[1]

#taking input of two values
x,y=[int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {} ".format(x,y))

      
