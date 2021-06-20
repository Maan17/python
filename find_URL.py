import re

def Find(string):
  #findall() has been used with valid conditions for urls in string
  url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
  return url

#driver code
string=input("Enter the string containing URL")
print("Urls:",Find(string))
