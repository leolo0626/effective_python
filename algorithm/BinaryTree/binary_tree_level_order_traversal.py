from collections import deque

def level_order(root):

    result = []
    if root is None:
        return result

    queue = deque([root])
    level = 0
    while root :
        result.append([])
        level_length = len(queue)

        for q in range(level_length):
            node = queue.popleft()
            result[level].append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level += 1

    return result