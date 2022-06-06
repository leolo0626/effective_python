class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sorted_array_to_bst(nums) :
    def helper(left, right):
        if left > right :
            return None

        mid = (left + right) //2
        root = Node(nums[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)
        return root
    return helper(0, len(nums)-1)
