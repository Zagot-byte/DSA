class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print(f"Inserted root node: {data}")
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
                print(f"Inserted {data} to left of {current.data}")
            else:
                self._insert(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
                print(f"Inserted {data} to right of {current.data}")
            else:
                self._insert(current.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        elif key < node.data:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

# Usage example:
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(15)
bt.insert(25)

print("Inorder Traversal:")
bt.inorder(bt.root)
print("\nPreorder Traversal:")
bt.preorder(bt.root)
print("\nPostorder Traversal:")
bt.postorder(bt.root)

found = bt.search(bt.root, 15)
print(f"\nSearch 15: {'Found' if found else 'Not Found'}")