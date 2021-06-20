from fractions import Fraction

#returning fraction value
print ("Fractions from 2 nos.:",Fraction(11,35))
print ("Fraction when argument is null:",Fraction())
print("Fraction when argument is float number:",Fraction(1.13))
print(Fraction('1.13'))

#returning the closest Fraction to self that has denominator atmost max_denominator
print ("Without limit:",Fraction('3.14159265358979323846'))
print ("With 1000 limit:",Fraction('3.14159265358979323846').limit_denominator(1000))
print ("With 100 limit:",Fraction('3.14159265358979323846').limit_denominator(100))
print ("With 10 limit:",Fraction('3.14159265358979323846').limit_denominator(10))

#returning lowest term
#returning numerator
print("Lowest Numerator term:",Fraction(125,50).numerator)
#returning denominator
print("Lowest Denominator term:",Fraction(125,50).denominator)
