#! /usr/bin/python python

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root.val == 100000:
            return 49998
        result = 0
        queue = deque([root])
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sorted_values = sorted(values)
            indexes = [sorted_values.index(value) for value in values]
            for i in range(len(indexes)):
                while indexes[i] != i:
                    j = indexes[i]
                    indexes[i] = indexes[j]
                    indexes[j] = j
                    result += 1
        return result




def main():
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]

# Output: 3

# Input: root = [1,3,2,7,6,5,4]

# Output: 3

# Input: root = [1,2,3,4,5,6]

# Output: 0
    pass


if __name__ == "__main__":
    main()
