pos=-1#global variable
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i#local variable to affect the value of global variable
            return True
        i=i+1
    return False
list=input().split()
n=input("Enter the number to be searched: ")
if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")
