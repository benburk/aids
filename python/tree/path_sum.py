"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Found in:
    https://leetcode.com/problems/path-sum/
"""


class TreeNode:
    """A node in a tree"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def has_path_sum(root: TreeNode, value) -> bool:
    """has path sum iterative"""
    if root is None:
        return False
    stack = [(root, value - root.data)]
    while stack:
        current, value = stack.pop()
        if value == 0 and current.left is None and current.right is None:
            return True
        if current.left is not None:
            stack.append((current.left, value - current.left.data))
        if current.right is not None:
            stack.append((current.right, value - current.right.data))
    return False


def test():
    """run test cases"""
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    assert has_path_sum(root, 22)


if __name__ == "__main__":
    test()
