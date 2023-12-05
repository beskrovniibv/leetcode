#! usr/bin/python

# 112. Path Sum

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = []
        queue.append((root, root.val))
        while len(queue) > 0:
            node, sum = queue.pop()
            if not node:
                continue
            if not node.left and not node.right:
                if sum == targetSum:
                    return True
            if node.left:
                queue.append((node.left, sum + node.left.val))
            if node.right:
                queue.append((node.right, sum + node.right.val))
        return False


if __name__ == '__main__':
    # case 4
    target = 1
    root = TreeNode(1)
    root.left = TreeNode(2)

    solution = Solution()
    answer = solution.hasPathSum(root, target)
    print(answer)
