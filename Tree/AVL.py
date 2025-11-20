class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    # Returns height of node or 0 if node is None
    return node.height if node else 0

def get_balance(node):
    # Balance factor = height(left subtree) - height(right subtree)
    return get_height(node.left) - get_height(node.right) if node else 0

def left_rotate(x):
    # Diagram of Left Rotation:
    # Before:
    #     x
    #      \
    #       y
    #      / \
    #     T2 T3
    #
    # After rotation:
    #       y
    #      / \
    #     x  T3
    #    / \
    #   T1 T2

    y = x.right
    x.right = y.left
    y.left = x

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(y):
    # Diagram of Right Rotation:
    # Before:
    #       y
    #      /
    #     x
    #    / \
    #   T1 T2
    #        \
    #         T3
    # After:
    #     x
    #    / \
    #   T1  y
    #      / \
    #    T2  T3

    x = y.left
    y.left = x.right
    x.right = y

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert(root, value):
    # Standard BST insertion with diagrams for operations
    if not root:
        # For leaf node, no rotation or balancing
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left Case (Right Rotation)
    #    z                                   y
    #   / \                                /   \
    #  y   T4    Right Rotation(z)        x     z
    # / \        - - - - - - - - ->      / \   / \
    #x   T3                            T1  T2 T3 T4
    #/ \
    #T1 T2
    if balance > 1 and value < root.left.value:
        return right_rotate(root)

    # Right Right Case (Left Rotation)
    #    z                                y
    #   /  \                            /   \
    # T1    y   Left Rotation(z)      z     x
    #      /  \  - - - - - - - ->   / \   / \
    #     T2  x                    T1 T2 T3 T4
    #        / \
    #      T3 T4
    if balance < -1 and value > root.right.value:
        return left_rotate(root)

    # Left Right Case (Left rotate on left then right rotate on root)
    #    z                              z                           x
    #   / \                            / \                        /   \
    #  y   T4  Left Rotation (y)      x  T4  Right Rotation(z)   y     z
    # / \       - - - - - - - ->     / \     - - - - - - - ->  / \   / \
    #T1  x                         y  T3                     T1 T2 T3 T4
    #   / \                       / \
    # T2 T3                     T1 T2
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case (Right rotate on right then left rotate on root)
    #  z                            z                             x
    # / \                          / \                          /   \
    #T1  y   Right Rotation (y)  T1   x   Left Rotation(z)   z      y
    #   / \  - - - - - - - ->        / \ - - - - - - - ->  / \    / \
    #  x  T4                        T2  y                T1 T2  T3  T4
    # / \                              / \
    #T2 T3                            T3 T4
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def pre_order(root):
    if root:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)

root = None
for val in [20, 4, 15, 70, 50, 100, 80]:
    root = insert(root, val)
print("Pre-order traversal of AVL tree:")
pre_order(root)
print()
