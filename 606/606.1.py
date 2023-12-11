#! usr/bin/python

# 606. Construct String from Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ''
        queue = []
        queue.append((root, 'r'))
        while len(queue) > 0:
            node, position = queue.pop()
        return result


if __name__ == '__main__':
    # case 0
    # root = TreeNode(1)
    # case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # case 2
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.right = TreeNode(4)

    solution = Solution()
    answer = solution.tree2str(root)
    print(answer)
