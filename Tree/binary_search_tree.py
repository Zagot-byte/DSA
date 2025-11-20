class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right

    def delete(self, key):
        """Delete node by key, showing diagrams right in the code."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            # CASE 1: No children (leaf)
            if node.left is None and node.right is None:
                print(f"Deleting leaf node: {node.data}")
                # Before:
                #    [parent]
                #      /
                # [node]
                # After:
                #    [parent]
                #      /
                #    None
                return None

            # CASE 2: Only one child
            if node.left is None:
                print(f"Deleting {node.data} (has only right child)")
                # Before:
                #  [parent]
                #     \
                #   [node]
                #      \
                #    [child]
                # After:
                #  [parent]
                #     \
                #   [child]
                return node.right

            if node.right is None:
                print(f"Deleting {node.data} (has only left child)")
                # Before:
                #  [parent]
                #    /
                # [node]
                #   /
                # [child]
                # After:
                #  [parent]
                #    /
                # [child]
                return node.left

            # CASE 3: Two children
            print(f"Deleting {node.data} (has two children)")
            # Before:
            #   [node]
            #  /      \
            # [left] [right]
            # Find inorder successor:
            succ = node.right
            while succ.left:
                succ = succ.left
            # Swapping values:
            print(f"Replacing {node.data} with successor {succ.data}")
            # After swap:
            #   [succ.data]
            #  /          \
            # [left]    [right subtree where succ was]
            node.data = succ.data
            node.right = self._delete(node.right, succ.data)
            # After deletion of successor node:
            # [succ.data] has correct subtree structure
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

# Example usage:
bst = BinarySearchTree()
for v in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(v)
print("\nInitial BST inorder:")
bst.inorder(bst.root)
print("\n")

# CASE 1: Delete leaf node
bst.delete(5)
print("\nBST after deleting leaf (5):")
bst.inorder(bst.root)
print("\n")

# CASE 2: Delete node with one child
bst.delete(30)
print("\nBST after deleting one-child node (30):")
bst.inorder(bst.root)
print("\n")

# CASE 3: Delete node with two children
bst.delete(10)
print("\nBST after deleting two-child node (10):")
bst.inorder(bst.root)
print()
