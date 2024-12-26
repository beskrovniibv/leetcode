#! /usr/bin/python pyton

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root: Optional[TreeNode], row):
            if not root:
                return
            if len(result) <= row:
                result.append(root.val)
            result[row] = max(result[row], root.val)
            dfs(root.left, row + 1)
            dfs(root.right, row + 1)

        dfs(root, 0)
        return result


solution = Solution()
print(solution.largestValues(
    root=TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))))
)
