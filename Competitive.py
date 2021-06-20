arr = list(map(int,input().split())) #input the array
min = arr[0] 
max,k = 0, 0

#traverse the array till we don't find profit
for i in range(len(arr)): 
  #finding the minimum price to buy stocks
  if arr[i]<min:
    min = arr[i]
    k+=1
  #finding price greater than Cost Price
  if arr[i] > min:
    max = arr[i]
    break


if(k!=0):#if we have bought the stocks
  #finding maximum price to sell them
  for i in range(k+1, len(arr)):
    if arr[i] > max :
      max = arr[i]


if max<min:#if we have not gained any profit then print 0
  print(0)
else:#if we have gained profit then print the profit
  print(max-min)

#Time Complexity: O(n)+O(n) = O(n)
