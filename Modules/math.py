#importing sqrt() and factorial from module math
from math import sqrt,factorial

#if we simply do "import math"then math.sqrt(16) and math.factorial(6) are required.
print (sqrt(16))
print (factorial(6))

#import built-in module math
import math
#prints all the modules and functions present in math module
print (dir(math))

a=2.3

#returns smallest integral value greater than the number
print(math.ceil(a))

#return largest integer value greater then the number
print(math.floor(a))
      
b=-10
c=5

#returns the absolute value in floating         
print(math.fabs(b))

#returns the factorial of the number
print(math.factorial(c))

#returns the number with value c but sign b
print(math.copysign(c,b))

#returns the greatest common divisor of 2 numbers
print(math.gcd(c,b))

#returns the value e raised to the power c
print(math.exp(c))

#returns logarithimic value of a base c
print(math.log(a,c))

#returns log c with base 2(more accurate value than above)
print(math.log2(c))

#return log c with base 10(more accurate value than above)
print(math.log10(c))

#returns b raised to power c(b**c)
print(math.pow(b,c))

#returns sine value(value passed should be in radians)
print(math.sin(c))

#returns cosine value(value passed should be in radians)
print(math.cos(c))

#returns tangent value(value passed should be in radians)
print(math.tan(c))

#returns hypotenuse of the values(returns the value of sqrt(a*a+b*b))
print(math.hypot(a,b))

#converts value from radian to degrees
print(math.degrees(c))

#converts value from degrees to radians
print(math.radians(c))

#denotes +ve point infinity constant(-inf denotes -ve point infinity constant)
if(math.isinf(math.inf)):
  print("The number is +ve infinity")

#denotes "not a number" in python
if(math.isnan(math.nan)):
  print("The number is nan")





