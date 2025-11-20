class Node:
    def __init__(self,data):
        self.data=data
        print("\ncreating new node",data)
        self.next=None
        self.display()
    def display(self):
        print("in node:",self.data)
class Singly:
    def __init__(self):
        
        self.head=None
        
    def isEmpty(self):
        if(self.head == None):
            return False
    def insert(self,data):
        if(self.isEmpty()):
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new    
        if(self.isEmpty()):
            print("Nothing")
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            new=Node(data)
            current.next=new
            current.head=new
    def insertAt(self,data,index):
        if(self.isEmpty()):
            print("Nothing")
        else:
            current=self.head
            i=0
            for i in range(index-1):
                current=current.next
            new=Node(data)
            new.next=current.next
            current.next=new
    def delete(self):
        if(self.isEmpty()):
            print("nothing ot delete")
        self.head=self.head.next
    def deleteEnd(self):
        if(self.isEmpty()):
            print("nothing")
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=None
    def deleteAt(self,key):
        if(self.isEmpty()):
            print("nothing")
        else:
            current=self.head
            prev=self.head
            while current.data != key:
                prev=current
                current=current.next
            prev.next=current.next
            
    def display(self):
        current=self.head
        while current:
            print("",current.data,end="->")
            current=current.next
s= Singly()
s.insert(5)
s.insertEnd(6)
print("\ninsert at begging")
s.display()
s.insertAt(4,1)
print("\ninsert at index")
s.display()
s.delete()
s.display()
s.insertAt(54,1)
print("\n----------------------------------")
s.deleteAt(54)
s.display()