"""
Check if a tree is a BST
"""


class TreeNode:
    """Tree node"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"


def is_bst(root, left=None, right=None):
    """bst"""
    if root is None:
        return True

    if left is not None and root.data <= left.data:
        return False

    if right is not None and root.data >= right.data:
        return False

    # check recursively for every node.
    return is_bst(root.left, left, root) and is_bst(root.right, root, right)


def test():
    """run test cases"""
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(4)
    assert not is_bst(root)

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    assert is_bst(root)


if __name__ == "__main__":
    test()
