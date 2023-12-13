#! usr/bin/python

# 144. Binary Tree Preorder Traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop()
            if not node:
                continue
            result.append(node.val)
            queue.append(node.right)
            queue.append(node.left)
        return result
