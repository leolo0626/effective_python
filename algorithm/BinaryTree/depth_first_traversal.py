from Node import Node

def depth_first_value(root):
    result = []
    if root is None :
        return result
    stack = [root]
    while stack :
        cur_node = stack.pop()
        result.append(cur_node.val)

        if cur_node.right is not None :
            stack.append(cur_node.right)

        if cur_node.left is not None :
            stack.append(cur_node.left)


    return result



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

    print(depth_first_value(a))