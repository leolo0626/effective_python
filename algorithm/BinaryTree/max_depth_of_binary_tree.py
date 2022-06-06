
def max_depth_of_binary_tree(root):
    if root is None:
        return 0
    return max(max_depth_of_binary_tree(root.left), max_depth_of_binary_tree(root.right)) + 1
