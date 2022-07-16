"""
Given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Found in:
    https://leetcode.com/problems/add-two-numbers/

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


def add_linked_numbers(node1: ListNode, node2: ListNode) -> ListNode:
    """
    Add two numbers represented as reversed linked lists
    time: O(n)
    space: O(n)
    """
    current = head = ListNode(0)
    total = 0
    while node1 or node2:
        if node1:
            total += node1.data
            node1 = node1.next
        if node2:
            total += node2.data
            node2 = node2.next
        total, remainder = divmod(total, 10)
        current.next = ListNode(remainder)
        current = current.next

    if total // 10:  # is there a carry at the end?
        current.next = ListNode(1)
    return head.next


def test():
    """run test cases"""
    list1 = ListNode(2, ListNode(4, ListNode(3)))
    list2 = ListNode(5, ListNode(6, ListNode(4)))

    assert str(add_linked_numbers(list1, list2)) == "7->0->8"


if __name__ == "__main__":
    test()
