
from Node import Node

def binary_tree_max_subarr(root):
    if root is None :
        return float("-inf")
    if root.left is  None and root.right is  None :
        return root.val

    return max(binary_tree_max_subarr(root.left), binary_tree_max_subarr(root.right)) + root.val





if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(binary_tree_max_subarr(a))