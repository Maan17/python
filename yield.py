#a generator function that yields 1 for 1st time,2 for 2nd time & 3 for 3rd time
def simpleGeneratorFun():
  yield 1
  yield 2
  yield 3

#driver code to check above generator function
for value in simpleGeneratorFun():
  print(value)

#generate squares from 1 to 100 using yield and generator.
def nextSquare():
  i=1;

  #an infinite loop to generate squares
  while True:
    yield i*i
    i+=1#next execution resumes from this point

#driver code to test above generator function
for num in nextSquare():
  if num>100:
    break
  print(num)
  
