#! usr/bin/python

# 110. Balanced Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.calcHeight(root.left)
        if left_height == -1:
            return -1
        right_height = self.calcHeight(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calcHeight(root) != -1


if __name__ == '__main__':
    # example 1
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # example 2
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(4)
    # example 3
    # root = None
    # example 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    root.right.left = TreeNode(6)
    solution = Solution()
    answer = solution.isBalanced(root)
    print(('false', 'true')[answer])
