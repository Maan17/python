def my_function():
  """Demonstrate docstrings and docs nothing really."""

  return None

print ("Using __doc__:")
print (my_function.__doc__)

print ("Using help:")
help(my_function)

#oneline docstring
print("\nOneline docstring")
def power(a,b):
  """"returns arg1 raised to power arg2"""
  return a**b

print (power.__doc__)

#multiline docstring
print("\nMultiline docstring")
def my_function(arg1):
  """
  Summary line.

  Extended description of function.

  Parameters:
  arg1(int):Description of arg1

  Returns:
  int: Description of return value

  """

  return arg1

print (my_function.__doc__)

#docstrings in classes
print("Docstrings in classes")
class ComplexNumber:
  """
  This is a class for mathematical operations on complex numbers.

  Attributes:
         real(int):The real part of complex number.
         imag(int):The imaginary part of complex number.
  """

  def __init__(self,real,imag):
    """
    The constructor for ComplexNumber class.

    Parameters:
          real(int):The real part of complex number.
          imag(int):The imaginary part of complex number.
     """

  def add(self,num):
    """
    The constructor for ComplexNumber class.

    Parameters:
          num(ComplexNumber):The complex number to be added.

     Returns:
           ComplexNumber:A Complex number which contains the sum

    """

    re=self.real+num.real
    im=self.imag+num.imag

    return ComplexNumber(re,im)

help(ComplexNumber)#to access Class docstring
help(ComplexNumber.add)#to access method's docstring


    
    


