#function to illustrate break in loop
def breakTest(arr):
  for i in arr:
    if i==5:
      break
    print(i)

#function to illustrate continue in loop
def continueTest(arr):
  for i in arr:
    if i==5:
      continue
    print (i),

#function to illustrate pass
def passTest(arr):
  pass

#Driver program to test above function

#Array to be used for above function
arr=[1,2,3,4,5,6,7]
print("The array is:",arr)

#break
print("Break method output")
breakTest(arr)

#continue
print("Continue method output")
continueTest(arr)

#illustrate pass-does nothing
passTest(arr)
