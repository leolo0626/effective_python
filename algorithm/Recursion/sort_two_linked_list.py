class Node :
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self.next is not None :
            return f"Node({self.val}) -> {self.next}"
        return f"Node({self.val})"

def sorted_merge(a : Node, b : Node) -> Node :
    if a is None :
        return b
    if b is None :
        return a

    if a.val < b.val :
        a.next = sorted_merge(a.next, b)
        return a
    else :
        b.next = sorted_merge(a, b.next)
        return b

if __name__ == "__main__":
    linked_list_1 = Node(1)
    linked_list_1.next = Node(8)
    linked_list_1.next.next = Node(22)
    linked_list_1.next.next.next = Node(40)

    linked_list_2 = Node(4)
    linked_list_2.next = Node(11)
    linked_list_2.next.next = Node(16)
    linked_list_2.next.next.next = Node(20)

    print(sorted_merge(linked_list_1, linked_list_2))