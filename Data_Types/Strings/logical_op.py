str1=''
str2='geeks'

#repr is used to print the string along with the quotes
print(repr(str1 and str2))     #returns str2
print(repr(str2 and str1))     #returns str1
print(repr(str1 or str2))       #returns str1
print(repr(str2 or str1))       #returns str2

str1='geeks'

print(repr(not str1))             #returns False

str1=''

print(repr(not str1))             #returns True
