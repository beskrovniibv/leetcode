#! usr/bin/python

# 145. Binary Tree Postorder Traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = [(root, False)]
        while len(queue) > 0:
            node, visited = queue.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    queue.append((node, True))
                    queue.append((node.right, False))
                    queue.append((node.left, False))
        return result


if __name__ == '__main__':
    # case 33
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    # case N
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)

    solution = Solution()
    ans = solution.postorderTraversal(root)
    print(*ans)
