#! usr/bin/python

# 101. Symmetric Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append((root.left, root.right))
        while len(queue) > 0:
            left, right = queue.pop()
            if left is None and right is None:
                continue
            if (left is None and right is not None) or (left is not None and right is None):
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


if __name__ == '__main__':
    # example 1
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)

    # example 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    solution = Solution()
    answer = solution.isSymmetric(root)
    print(('false', 'true')[answer])
