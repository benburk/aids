"""
Merge k sorted linked lists and return it as one sorted list.
"""
from collections import deque


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


def merge_lists(lists):
    """divide and conquer
    time: O(nlogk)
    """
    lists = deque(lists)

    def merge(node1, node2):
        """merge two sorted linked lists
        time: O(n)
        """
        current = head = ListNode(0)  # create dummy head to attach to
        while node1 and node2:
            if node1.data < node2.data:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next
        if node1:
            current.next = node1
        elif node2:
            current.next = node2

        return head.next

    while len(lists) > 1:
        lists.append(merge(lists.popleft(), lists.popleft()))

    return lists[0]


def test():
    """run test cases"""
    lists = (
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    )

    print(merge_lists(lists))


if __name__ == "__main__":
    test()
