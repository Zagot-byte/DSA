class Node:
    def __init__(self, data):
        self.data = data
        print("\ncreating new node", data)
        self.next = None
        self.prev = None
        self.display()
    def display(self):
        print("in node:", self.data)

class Doubly:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insertEnd(self, data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
            new.prev = current

    def insertAt(self, data, index):
        if self.isEmpty() and index > 0:
            print("List is empty, cannot insert at index", index)
            return
        new = Node(data)
        if index == 0:
            self.insert(data)
        else:
            current = self.head
            i = 0
            while i < index - 1 and current is not None:
                current = current.next
                i += 1
            if current is None:
                print("Index out of bounds")
                return
            new.next = current.next
            if current.next is not None:
                current.next.prev = new
            current.next = new
            new.prev = current

    def delete(self):
        if self.isEmpty():
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteEnd(self):
        if self.isEmpty():
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.prev.next = None

    def deleteAt(self, key):
        if self.isEmpty():
            print("Nothing to delete")
            return
        current = self.head
        while current is not None and current.data != key:
            current = current.next
        if current is None:
            print("Key not found")
            return
        if current.prev is None:  # Deleting head
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
        else:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev

    def display(self):
        current = self.head
        while current:
            print("", current.data, end="<->")
            current = current.next
        print("None")

# Example usage
d = Doubly()
d.insert(5)
d.insertEnd(6)
print("\ninsert at beginning")
d.display()
d.insertAt(4,1)
print("\ninsert at index")
d.display()
d.delete()
d.display()
d.insertAt(54,1)
print("\n----------------------------------")
d.deleteAt(54)
d.display()
