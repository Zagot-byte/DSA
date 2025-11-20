class Node:
    def __init__(self, data):
        self.data = data
        print("\nCreating new node:", data)
        self.next = None
        self.prev = None
        self.display()
    def display(self):
        print("In node:", self.data)

class Doubly:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, data):
        # Insert at beginning
        new = Node(data)
        if self.isEmpty():
            self.head = new
            # Diagram: [data] <-> None
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
            # Diagram: [data] <-> [old head] <-> ... <-> None

    def insertEnd(self, data):
        # Insert at end
        new = Node(data)
        if self.isEmpty():
            self.head = new
            # Diagram: [data] <-> None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
            new.prev = current
            # Diagram: ... <-> [current] <-> [data] <-> None

    def insertAt(self, data, index):
        # Insert at specific index
        if self.isEmpty() and index > 0:
            print("List is empty, cannot insert at index", index)
            return
        new = Node(data)
        if index == 0:
            self.insert(data)
            # Diagram: [data] <-> [old head] <-> ... <-> None
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
            # Diagram: ... <-> [current] <-> [data] <-> [current.next] <-> ...

    def delete(self):
        # Delete from beginning (pop head)
        if self.isEmpty():
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            # Diagram: None
        else:
            self.head = self.head.next
            self.head.prev = None
            # Diagram: [new head] <-> ... <-> None

    def deleteEnd(self):
        # Delete from end
        if self.isEmpty():
            print("Nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            # Diagram: None (list is empty)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            print(f"Deleting node: {current.data}")
            current.prev.next = None
            # Diagram: ... <-> [current.prev] <-> None

    def deleteAt(self, key):
        # Delete node by value
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
            # Diagram: [new head] <-> ... <-> None
        else:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            # Diagram: ... <-> [current.prev] <-> [current.next] <-> ...

    def display(self):
        # Draw the whole list as a double-arrow
        current = self.head
        print("List:", end=" ")
        while current:
            print(f"[{current.data}]", end="<->")
            current = current.next
        print("None")

# Example usage (with step-by-step diagrams)
d = Doubly()
d.insert(5)
# Diagram: [5] <-> None

d.insertEnd(6)
# Diagram: [5] <-> [6] <-> None

print("\nInsert at beginning")
d.display()

d.insertAt(4,1)
print("\nInsert at index 1")
# Diagram: [5] <-> [4] <-> [6] <-> None
d.display()

d.delete()
# Diagram: [4] <-> [6] <-> None
d.display()

d.insertAt(54,1)
print("\nInsert at index 1 (after delete)")
# Diagram: [4] <-> [54] <-> [6] <-> None
d.display()

print("\n----------------------------------")
d.deleteAt(54)
# Diagram: [4] <-> [6] <-> None
d.display()
