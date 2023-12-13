#! usr/bin/python

# 1464. Maximum Product of Two Elements in an Array

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1)*(nums[-2] - 1)
