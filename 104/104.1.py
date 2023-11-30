#! usr/bin/python

# 104. Maximum Depth of Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = []
        queue.append((root, 1))
        while len(queue) > 0:
            node, level = queue.pop()
            if not node:
                continue
            answer = max(answer, level)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        return answer


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    answer = solution.maxDepth(root)
    print(answer)
