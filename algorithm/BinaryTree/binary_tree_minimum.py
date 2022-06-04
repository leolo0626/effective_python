
from Node import Node

def binary_tree_recursive_min(root):
    if root is None:
        return float('inf')

    return min(binary_tree_recursive_min(root.left), binary_tree_recursive_min(root.right), root.val)





if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(15)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(binary_tree_recursive_min(a))