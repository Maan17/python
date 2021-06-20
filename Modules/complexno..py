#import cmath for complex number operations
import cmath

#initializing real numbers
x=5
y=3
print("The real numbers are:",x,y)

#converting x and y into complex number
z=complex(x,y);
print("The complex number is:",z)

#printing real and imaginary part of complex number
print("The real part of complex number is:",z.real)
print("The imaginary part of complex number is:",z.imag)

#converting complex number into polar using polar()
w=cmath.polar(z)

#printing modulus and argument of polar complex number
print("The modulus and argument of polar complex number is:",w)

#converting complex number into rectangular using rect()
w=cmath.rect(5.830951894845301,0.5404195002705842)
print("The rectangular form of complex number is:",w)

#printing exponent of complex number
print("The exponent of complex number is:",cmath.exp(z))

#printing log form of complex number
print("The log(base 2) of complex number is:",cmath.log(z,2))

#printing log10 of complex number
print("The log10 of complex number is:",cmath.log10(z))

#printing square root of complex number
print("The square root of complex number is:",cmath.sqrt(z))

#checking if both numbers are finite
if cmath.isfinite(z):
  print("Complex number is finite")

#checking if either number is/are infinte
if cmath.isinf(z):
  print("Complex number is infinite")

#checking if either number is/are infinite
if cmath.isnan(z):
  print("Complex number is NaN")

#printing the value of pi
print("The value of pi is:",cmath.pi)

#printing the value of e
print("The value of exponent is:",cmath.e)

#sine of complex number
print("The sine of complex number is:",cmath.sin(z))

#cosine of complex nymber
print("The cosine of complex number is:",cmath.cos(z))

#tangent of complex number
print("The tangent of complex number is:",cmath.tan(z))

#tangent arc sine of complex number
print("The arc sine of complex number is:",cmath.asin(z))

#printing arc cosine of complex number
print("The arc cosine of complex number is:",cmath.acos(z))

#printing arc tangent of complex number
print("The arc tangent of complex number is:",cmath.atan(z))

#printing hyperbolic sine of complex number
print("The hyperbolic sine of complex number is:",cmath.sinh(z))

#printing hyperbolic cosine of complex number
print("The hyperbolic cosine of complex number is:",cmath.cosh(z))

#printing hyperbolic tangent of complex number
print("The hyperbolic tangent of complex number is:",cmath.tanh(z))

#printing inverse hyperbolic sine of complex number
print("The inverse hyperbolic sine of complex number is:",cmath.asinh(z))

#printing inverse hyperbolic cosine of complex number
print("The inverse hyperbolic cosine of complex number is:",cmath.acosh(z))

#printing inverse hyperbolic tangent of complex number
print("The inverse hyperbolic tangent of complex number is:",cmath.atanh(z))


