#import built in module datetime
import datetime
from datetime import date
import time

#Returns the number of seconds
#since jan 1st,1970
print (time.time())

#converts number of seconds to a date
print (date.fromtimestamp(8495823748))

#using MINYEAR to print minimum representable year
print("Minimum representable year is:",datetime.MINYEAR)

#using MAXYEAR to print minimum representable year
print("Maximum representable year is:",datetime.MAXYEAR)

#using date() to represent date
print("The represented date is:",datetime.date(2019,4,5))

#using today() to print present date
print("Present date is:",date.today())

#using min() to print minimum representable date
print("Minimum representable date is",date.min)

#using max() to print maximum representable date
print("Maximum representable date is",date.max)
