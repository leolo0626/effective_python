from Node import Node
from collections import deque

def breath_first_values(root):
    queue = deque([root])
    result = []
    while queue :
        cur_node = queue.popleft()
        print(cur_node)
        result.append(cur_node.val)
        if cur_node.left is not None :
            queue.append(cur_node.left)

        if cur_node.right is not None :
            queue.append(cur_node.right)

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

    print(breath_first_values(a))
