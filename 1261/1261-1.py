#! /usr/bin/env python

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()

        def p(node, value):
            if not node:
                return
            node.val = value
            self.nums.add(value)
            p(node.left, value*2 + 1)
            p(node.right, value*2 + 2)

        p(root, 0)

    def find(self, target: int) -> bool:
        return target in self.nums


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)