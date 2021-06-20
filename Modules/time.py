#importing time module from time operations
import time

#using time() to display time since epoch
print("Seconds elapsed since epoch are:",time.time())

#using gmtime() to return the time attribute structure
ti=time.gmtime()
print("Time calculated according to given seconds is:",ti)

#using asctime() to display time according to time mentioned
print("Time calculated using asctime() is:",time.asctime(ti))

#using ctime() to display present time
print("Start execution:",time.ctime())

#using sleep() to hault execution
time.sleep(4)

#using ctime() to show present time
print("Stop Execution:",time.ctime())

from datetime import  *

#prints in date and time format
print(datetime(2019,11,23,10,23,10))

#prints the day,moth and year of given time
s=datetime(2019,11,23,10,23,10)
print(s.day)
print(s.month)
print(s.year)

#prints current time
print(datetime.now())

#subtracting present time with some other time
now=datetime.today()
other=datetime(1997,7,20,22,56)
print(now-other)





