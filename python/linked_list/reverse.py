"""
Reverse a linked list
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


def reverse(head):
    """Reverse a linked list in one pass
    time: O(n)
    """
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


def test():
    """run test cases"""
    head = ListNode(5, ListNode(3, ListNode(2)))
    assert str(reverse(head)) == "2->3->5"


if __name__ == "__main__":
    test()
