import string
#appending a string
a='Geeks'
print(a)
print("Id of string a:",id(a))
a=a+'for'
print(a)
print("Id of string a:",id(a))

#both string hold same identity
string1="Hello"
string2="Hello"
print("\nString1 is:",string1)
print("String2 is:",string2)
print("ID of string1 is:",id(string1))
print("ID of string2 is:",id(string2))

#string with single quotes
a='Geeks'
#string with double quotes
b="for"
#string with triple quotes
c='''Geeks a portal for geeks'''
d='''He said,I'm fine.'''
print("\nString with single quotes",a)
print("String with double quotes",b)
print("String with triple quotes",c)
print("String with triple quotes",d)
#concatenation of string using different quotes
print("Concatenation of strings:",a+b+c)

#printing quotes
#use of escape sequence
print("\nHe said,\"Welcome to GFG\" ")
#use of mix quotes
print('Getting Geeky,"Loving it"')

#printing escape character
print("\n\\ is back slash")

#slicing in strings
s=str(input("\nEnter the string:"))
print("Third character is:",s[2])
print("Fourth to Tenth character:",s[4:10:2])

#STRING METHODS
str1="Geeksforgeeks is for Geeks"
str2="Geeks"
print(str1)
print(str2)

#find() and rfind()

#using find() to find first occurrence of str2
print("\nThe first occurence of str2 is at:",str1.find(str2,4))

#using rfind() to find last occurrence of str2
print("The last occurence of str2 is at:",str1.find(str2,4))

#startswith() and endswith()

#using startswith() to find if str1 begins with str2
if str2.startswith(str1):
  print("\nstr1 begins with:"+str2)
else:
  print("\nstr1 does not begin with:"+str2)
  
#using endswith() to find if str1 ends with str2
if str2.endswith(str1):
  print("\nstr1 ends with:"+str2)
else:
  print("\nstr1 does not ends with:"+str2)

#isupper() and islower()
  
#checking if all charachters in str1 are upper cased
if str1.isupper():
  print("\nAll characters in str1 are uppercased")
else:
  print("\nAll characters in str1 are not uppercased")

#checking if all charachters in str1 are lower cased
if str1.islower():
  print("\nAll characters in str1 are lowercased")
else:
  print("\nAll characters in str1 are not lowercased")

#converting string into it's lower case
str3=str1.lower();
print("\nLowercase converted string is:"+str3)

#converting string into it's upper case
str4=str1.upper();
print("\nUppercase converted string is:"+str4)

#converting string into it's swapped case
str5=str1.swapcase();
print("\nThe swap case converted string is:"+str5)

#converting string into it's titlecase
str6=str1.title();
print("\nThe title case converted string is:"+str6)

#printing length of the string using len()
print("\nThe length of string is:",len(str1))

#printing the occurence by count()
print("\nNumber of appearance of \"geeks\"is:",str1.count("geeks",0,26))

#printing the string after centering with '-'
print("\nThe string after centering with '-' is:",str1.center(26,'-'))

#printing the string after ljust() 
print("\nThe string after ljust() is:",str1.ljust(26,'-'))

#printing the string after rjust() 
print("\nThe string after rjust() is:",str1.rjust(26,'-'))

#checking if str1 has all alphabets
if str1.isalpha():
  print("\nAll characters are alphabets in str1")
else:
  print("\nAll characters are not alphabets in str1")

#checking if str1 has all numbers
if str1.isalnum():
  print("\nAll characters are numbers in str1")
else:
  print("\nAll characters are not numbers in str1")

#checking if str1 has all spaces
if str1.isspace():
  print("\nAll characters are spaces in str1")
else:
  print("\nAll characters are not spaces in str1")

#using join() to join str1 with str2
print('\nThe string after joining is:',str1.join(str2))

#using strip() to delete all '-'
print("\nString after stripping all '-' is:",str1.strip('-'))

#using lstrip() to delete all trailing '-'
print("\nString after stripping all leading '-' is:",str1.lstrip('-'))

#using rstrip() to delete all trailing '-'
print("\nString after stripping all trailing '-' is:",str1.rstrip('-'))

#using min() to print the smallest character
print("\nThe minimum value character is:",min(str1))

#using max() to print largest character
print("\nThe maximum value charater is:",max(str1))

str3="gfo"
str4="abc"

#using maktrans() to m to map elements of str4 with str3
mapped=str.maketrans(str3,str4)
#using translate() to translate using the mapping
print("\nThe string after translation using mapped element:",str1.translate(mapped))

str5="geeks"
str6="nerds"

#using replace() to replace str5 with str6 in str1
#only changes two occurences
print("\nThe string after replacing strings is:",str1.replace(str5,str6,2))

string='GEEKS\tFOR\tGEEKS'
print(string.expandtabs(2))

#convering string to list
str7="Geeks-for-Geeks"
li=list(str7.split())
print(li)

      
