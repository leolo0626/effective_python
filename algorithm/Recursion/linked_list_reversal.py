class Node :
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self.next is not None :
            return f"Node({self.val}) -> {self.next}"
        return f"Node({self.val})"

def reverse_linked_list(head):
    if head is None or head.next is None :
        return head
    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return p

if __name__ == "__main__":
    A = Node(1)
    B = Node(2)
    C = Node(3)
    A.next = B
    B.next = C
    print(reverse_linked_list(A))