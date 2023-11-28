#! usr/bin/python

# 100. Same Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        vertexes = []
        vertexes.append((p, q))
        while len(vertexes) > 0:
            f, s = vertexes.pop()
            if f is None and s is None:
                continue
            if (f is not None and s is None) or (f is None and s is not None):
                return False
            if f.val != s.val:
                return False
            vertexes.append((f.left, s.left))
            vertexes.append((f.right, s.right))
        return True


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    solution = Solution()
    answer = solution.isSameTree(p, q)
    print(('false', 'true')[answer])
