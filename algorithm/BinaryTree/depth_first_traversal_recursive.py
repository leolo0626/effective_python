from Node import Node

def depth_first_traversal_recursive(root, arr=[]) :
    if root is None :
        return arr

    arr.append(root.val)

    if root.left is not None :
        depth_first_traversal_recursive(root.left, arr)

    if root.right is not None:
        depth_first_traversal_recursive(root.right, arr)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    result = []
    depth_first_traversal_recursive(a, result)
    print(result)