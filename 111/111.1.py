#! usr/bin/python

# 111. Minimum Depth of Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        queue = []
        queue.append((root, 0))
        while len(queue) > 0:
            node, height = queue.pop()
            if node:
                if not node.left and not node.right:
                    result = min(result, height + 1) if result else (height + 1)
                queue.append((node.left, height + 1))
                queue.append((node.right, height + 1))
        return result


if __name__ == '__main__':
    # example 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # example 2
    # root = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    # root.right.right.right.left = TreeNode(6)

    solution = Solution()
    answer = solution.minDepth(root)
    print(answer)
