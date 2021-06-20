pos=-1#global variable
lists=input().split()
n=input("Enter the number to be searched: ")

if search(lists,n):
    print("Found at",pos+1)
else:
    print("Not Found")

def search(lists,n):

    l=0
    u=len(lists)-1

    while l<=u:
        mid=(l+u)//2

        if lists[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lists[mid]<n:
                l=mid+1
            else:
                u=mid-1

