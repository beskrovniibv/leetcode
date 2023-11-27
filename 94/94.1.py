#! usr/bin/python

# 94. Binary Tree Inorder Traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        answer = []
        vertexes = []
        proceed = []
        vertexes.append(root)
        proceed.append(True)
        while len(vertexes) > 0:
            v = vertexes.pop()
            p = proceed.pop()
            if v is not None:
                if p:
                    vertexes.append(v)
                    proceed.append(False)
                    vertexes.append(v.left)
                    proceed.append(True)
                else:
                    answer.append(v.val)
                    vertexes.append(v.right)
                    proceed.append(True)
        return answer


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    answer = solution.inorderTraversal(root)
    print(*answer)
