from Node import Node

def binary_tree_recursive_sum(root):
    if root is None:
        return 0
    return binary_tree_recursive_sum(root.left) + binary_tree_recursive_sum(root.right) + root.val



if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(binary_tree_recursive_sum(a))
