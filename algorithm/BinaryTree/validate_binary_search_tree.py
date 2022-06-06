

def check_if_valid(root, min_range, max_range):
    if root is None:
        return True

    if root.val >= min_range or root.val <= max_range:
        return False

    return check_if_valid(root.left, min_range, root.val) and check_if_valid(root.right, root.val, max_range)

