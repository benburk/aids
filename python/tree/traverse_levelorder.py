"""binary tree"""


class TreeNode:
    """Tree node"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"

    def __iter__(self):
        """iterate through a tree level by level"""
        queue = [self]
        next_level = []
        while queue:
            current = queue.pop(0)
            yield current
            for child in (current.left, current.right):
                if child is not None:
                    next_level.append(child)
            if not queue:
                print("---")
                queue.extend(next_level)
                next_level = []


def test():
    """run test cases"""
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    for node in root:
        print(node)


if __name__ == "__main__":
    test()
