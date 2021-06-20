class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
if __name__=='__main__':
     arr=input("Enter the linked list").split()
     llist=LinkedList()
     llist.head=Node(arr[0])
     temp=llist.head
     for i in range(1,len(arr)):
         temp.data=Node(arr[i])
         temp.next=temp.data
         temp=temp.next
     llist.printList()
