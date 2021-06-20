import re
from re import *

#compile() creates regular expression character
p=re.compile('[a-e]')
#findall() searches for the regular expression and returns a list
print(p.findall("Aye,said Mr. Gibenson Stark"))

#\d is equivalent to [0-9]
p=re.compile('\d')
print("\n",p.findall("I went to him at 11 A.M. on 4th July 1886"))
#\d+ will match a group on [0-9],group of one or greater size
p=re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July  1886"))

#\w is equivalent to [a-z A-Z 0-9]
p=re.compile('\w')
print("\n",p.findall("He said * in some_lang."))
#\w+ matches to group of alphanumeric character
p=re.compile('\w+')
print(p.findall("I went to him at 11 A.M.,he said *** in some_language."))
#\W matches to non alphanumeric characters.
p=re.compile('\W')
print(p.findall("He said *** in some language"))

#'*' replaces the number of occurences of a character
p=re.compile('ab*')
print("\n",p.findall("ababbaabbb"))

#'\W+' denotes non-alphanumeric characters or a group of characters
#Upon finding non-alphanumeric group of characters,the split(),splits the string from that point
print("\n",split('\W+','Words, words , Words'))
print(split('\W+',"Word's, words , Words"))
print(split('\W+','On 12th Jan 2016,at 11:02 AM'))
#'\d+' denotes numeric characters or group of characters
#splitting ocurrs at numeric characters
print(split('\d+','On 12th Jan 2016,at 11:02 AM'))
#splitting occurs only once, at '12',returned list will have length 2
print(split('\d+','On 12th Jan 2016,at 11:02 AM',1))
#'Boy' and 'boy' will be treated same when flags=re.IGNORECASE
print(re.split('[a-f]+','Aey,Boy oh boy,come here',flags=re.IGNORECASE))

#matching the pattern and replacing it with another string using sub()
print("\n",re.sub('ub','~*','Subject has Uber booked already',flags=re.IGNORECASE))
#case sensitivity will be considered
print(re.sub('ub','~*','Subject has Uber booked already'))
#max times replacement occursis 1
print(re.sub('ub','~*','Subject has Uber booked already',count=1,flags=re.IGNORECASE))
print(re.sub('And','&','Baked Beans And Spam',flags=re.IGNORECASE))

#using subn() to return a tuple with a count of total replacement and the new string
print("\n",re.subn('ub','~*','Subject has Uber booked already'))

#escape() returns string with a BackSlash '\',before every Non-Alphanumeric Character
print("\n",re.escape("This is awesome even 1 AM"))
print(re.escape("I asked what is this [a-9],he said \t ^WoW"))
