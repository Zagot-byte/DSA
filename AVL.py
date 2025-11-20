class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    # Rotations
    if balance > 1 and value < root.left.value:  # LL
        return right_rotate(root)
    if balance < -1 and value > root.right.value:  # RR
        return left_rotate(root)
    if balance > 1 and value > root.left.value:  # LR
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and value < root.right.value:  # RL
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def pre_order(root):
    if root:
        print(f"{root.value} ", end="")
        pre_order(root.left)
        pre_order(root.right)

# Example Usage:
root = None
for val in [20, 4, 15, 70, 50, 100, 80]:
    root = insert(root, val)
print("Pre-order:")
pre_order(root)