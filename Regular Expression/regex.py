import re

#creating regex objects
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#matching regex objects
mo=phoneNumRegex.search(input("Enter the number in (3)-(3)-(4) format:"))
print('Phone number found:',mo.group())

#grouping with parenthesis
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search(input("\nEnter the number:"))
#retrieving first group
print('\nArea-code:',mo.group(1))
#retrieving all the groups at once
areacode,mainNumber=mo.groups()
print('Areacode:',areacode,'Main Number:',mainNumber)

#matching with pipe
heroRegex=re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

#matching specific repitions
haRegex=re.compile(r'(Ha){3}')
mo1=haRegex.search('HaHaHa')
print(mo1.group())

#(wo)? is optional,it might be present or not
batRegex=re.compile(r'Bat(wo)?man')
mo1=batRegex.search('The Adventures of Batman')
print(mo1.group())

#(wo)* ,there can be any number of occurences
batRegex=re.compile(r'Bat(wo)*man')
mo2=batRegex.search('The Adventures of Batwoman')
print(mo2.group())

#matching one or more using +
batRegex=re.compile(r'Bat(wo)+man')
mo1=batRegex.search('The adventures of Batwoman')
print(mo1.group())
