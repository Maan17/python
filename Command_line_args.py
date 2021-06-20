import sys 
  
# total arguments 
n = len(sys.argv) 
Sum = 0
lst=[]
for i in range(1, n): 
    lst.append(sys.argv[i])
print("\n\nResult:", lst)
