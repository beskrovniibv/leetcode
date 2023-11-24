#! usr/bin/python

# 88. Merge Sorted Array

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, index = m - 1, n - 1, m + n - 1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] >= nums2[i2]:
                nums1[index] = nums1[i1]
                i1 -= 1
            else:
                nums1[index] = nums2[i2]
                i2 -= 1
            index -= 1
        while i2 >= 0:
            nums1[index] = nums2[i2]
            i2 -= 1
            index -= 1


if __name__ == '__main__':
    nums1 = list(map(int, input().split()))
    m = len(nums1)
    nums2 = list(map(int, input().split()))
    solution = Solution()
    nums1 = nums1 + [0] * len(nums2)
    solution.merge(nums1, m, nums2, len(nums2))
    print(*nums1)
