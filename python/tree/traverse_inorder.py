"""
traversal of binary tree
"""


class TreeNode:
    """Tree node
    with inorder traversal
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"

    def __iter__(self):
        """iterate through a tree inorder"""

        def in_order(root):
            if root:
                yield from in_order(root.left)
                yield root.data
                yield from in_order(root.right)

        yield from in_order(self)


def test():
    """run test cases"""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print([x for x in root])


if __name__ == "__main__":
    test()
