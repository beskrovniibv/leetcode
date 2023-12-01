#! usr/bin/python

# 108. Convert Sorted Array to Binary Search Tree

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if right < left:
            return None
        mid = (left + right)//2
        root = TreeNode(nums[mid])
        root.left = self.createTree(nums, left, mid - 1)
        root.right = self.createTree(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.createTree(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    array = [-10, -3, 0, 5, 9]
    solution = Solution()
    solution.sortedArrayToBST(array)
