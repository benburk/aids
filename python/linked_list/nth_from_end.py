"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""


class ListNode:
    """linked list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "->".join(str(x) for x in self)

    def __iter__(self):
        current = self
        while current:
            yield current.data
            current = current.next


def print_nth_from_end(head, n):
    front = head
    for _ in range(n):
        front = front.next
    end = head

    while front.next is not None:
        front = front.next
        end = end.next
    return end.data


def remove_nth_from_end(head, n):
    """
    One pass
    O(n)
    """
    front = head
    current = head
    # advance the pointer
    for _ in range(n):
        front = front.next
    if not front:
        return head.next

    while front:
        front = front.next
        if front:
            current = current.next

    current.next = current.next.next
    return head


def test():
    """run test cases"""
    head = ListNode(4, ListNode(5, ListNode(2, ListNode(3))))
    print(print_nth_from_end(head, 2))
    print(remove_nth_from_end(head, 2))


if __name__ == "__main__":
    test()
