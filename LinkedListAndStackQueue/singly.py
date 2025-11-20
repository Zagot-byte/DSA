class Node:
    def __init__(self, data):
        self.data = data
        print("\nCreating new node:", data)
        self.next = None
        self.display()

    def display(self):
        print("In node:", self.data)

class Singly:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        # Returns True if empty, False if not
        return self.head is None

    def insert(self, data):
        # Insert at the beginning (push operation)
        if self.isEmpty():
            self.head = Node(data)
            print("After insert (head):", self.head.data)
            # Diagram:
            # [data] -> None
        else:
            new = Node(data)
            new.next = self.head
            self.head = new
            print("After insert (push at beginning):")
            # Diagram:
            # [data] -> [previous head] -> ...
            self.display()

    def insertAt(self, data, index):
        # Insert at given index
        if index == 0:
            self.insert(data)
            print("After insert at index 0:")
            # Diagram:
            # [data] -> [previous head] -> ...
            self.display()
        else:
            current = self.head
            for _ in range(index - 1):
                if current is not None:
                    current = current.next
            if current is not None:
                new = Node(data)
                new.next = current.next
                current.next = new
                print(f"After insert at index {index}:")
                # Diagram:
                # ... -> [current] -> [data] -> [current.next] -> ...
                self.display()

    def delete(self):
        # Delete from beginning
        if self.isEmpty():
            print("Nothing to delete")
        else:
            print(f"Deleting node: {self.head.data}")
            self.head = self.head.next
            print("After delete at beginning:")
            # Diagram:
            # [previous head] -> [new head] -> ...
            self.display()

    def deleteEnd(self):
        # Delete from end
        if self.isEmpty():
            print("Nothing")
        else:
            current = self.head
            prev = None
            while current.next is not None:
                prev = current
                current = current.next
            if prev:
                print(f"Deleting node: {current.data}")
                prev.next = None
                # Diagram:
                # ... -> [prev] -> None
            else:
                # Only one node
                print(f"Deleting last node: {self.head.data}")
                self.head = None
            print("After delete at end:")
            self.display()

    def deleteAt(self, key):
        # Delete node by value
        if self.isEmpty():
            print("Nothing")
        else:
            current = self.head
            prev = None
            while current is not None and current.data != key:
                prev = current
                current = current.next
            if current is None:
                print(f"Node with data {key} not found")
            elif prev is None:
                # Head node to delete
                print(f"Deleting head node: {key}")
                self.head = current.next
            else:
                print(f"Deleting node: {key}")
                prev.next = current.next
            print("After delete value", key)
            # Diagram:
            # ... -> [prev] -> [deleted: key] -> [current.next] -> ...
            self.display()

    def display(self):
        current = self.head
        print("List:", end=" ")
        while current:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None")

# Usage example (with diagram comments for each step):
s = Singly()
s.insert(5)
# Diagram: [5] -> None
s.insert(6)
# Diagram: [6] -> [5] -> None
print("\nInsert at beginning")
s.display()

s.insertAt(4, 1)
print("\nInsert at index 1")
# Diagram: [6] -> [4] -> [5] -> None
s.display()

s.delete()
# Diagram: [4] -> [5] -> None (if last head deleted)
s.display()

s.insertAt(54, 1)
print("\nInsert at index 1 (after delete)")
# Diagram: [4] -> [54] -> [5] -> None
s.display()

print("\n----------------------------------")
s.deleteAt(54)
# Diagram: [4] -> [5] -> None (after deleting value 54)
s.display()
