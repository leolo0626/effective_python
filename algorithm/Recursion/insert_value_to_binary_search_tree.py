class Node :
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is not None and self.right is not None:
            return f"{self.left} <- Node({self.val}) -> {self.right}"

        if self.left is not None :
            return f"{self.left} <- Node({self.val}) -> None"

        if self.right is not None :
            return f"None <- Node({self.val}) -> {self.right}"

        return f"None <- Node({self.val}) ->None"

def insert_node(head, data) :
    if head is None :
        head = Node(data)
        return head

    if head.val < data :
        head.right = insert_node(head.right, data)
    else :
        head.left = insert_node(head.left, data)

    return head

if __name__ == "__main__":
    a = Node(1)
    a.left = Node(2)
    a.right = Node(7)

    print(insert_node(a, 10))
    print(insert_node(a, 6))