#setting a bit at nth position
num=int(input("Enter the number to be set: "))
n=int(input("Enter the position "))
print("The set bit at position is: ",num|(1<<n))

#unsetting a bit at nth position
num=int(input("Enter the number to be unset: "))
n=int(input("Enter the position "))
print("The unset bit at position is ",num&(~(1<<n)))

#toggling bit at nth position
num=int(input("Enter the number to be toggled: "))
n=int(input("Enter the position "))
print("The toggledbit at position is ",num^((1<<n)))

#checking if nth bit at position is set or unset
num=int(input("Enter the number to be checked for set or unset: "))
n=int(input("Enter the position "))
print(num&((1<<n)))

#inverting every bit of a number
num=int(input("Enter the number to be inverted: "))
print(~num)

#two's complement
num=int(input("Enter the number to find 2's complement: "))
print(~num+1)

#stripping off the lowest set bit
num=int(input("Enter the number to strip off the lowest set bit:  "))
print(num & num-1)

#getting lowest set bit of a number
num=int(input("Enter the number to get the lowest set bit"))
print(num & (~num+1))

#clear all bits from LSB to ith bit
num=int(input("Enter the number to clear all bits from LSB to ith bit: "))
n=int(input("Enter the position "))
print("The cleared no. is ",num &(~((1<<n+1)-1)))

#clear all bits from MSB to ith bit
num=int(input("Enter the number to clear all bits from MSB to ith bit: "))
n=int(input("Enter the position "))
print("The cleared no. is ",num &(~((1<<n)-1)))

#divide by two
num=int(input("Enter the number to divide by two"))
print(num>>1)

#multiply by two
num=int(input("Enter the number to multiply by two"))
print(num<<1)

#upper case to lower case
char=input("Enter the character to convert to lower case: ")
print(chr(ord(char)+32))

#lower case to lower case
char=input("Enter the character to convert to upper case: ")
print(chr(ord(char)-32))

#counting the number of set bits
num=int(input("Enter the number to count the number of set bits"))
count=0
while(num):
    num&=(num-1)
    count+=1
print(count)
#another method
count=bin(i).count('1')

#find log base 2 of a 32 bit integer
num=int(input("Enter the number to find log base 2"))
res=0
while(num):
    num=num>>1
    res+=1
print(res)

#checking if 32-bit integer is the power of 2
num=int(input("Enter the number to check for power of two"))
if (num &(num-1))==0:
    print("Yes")
else:
    print("No")
    
    
