#! usr/bin/python

# 35. Search Insert Position

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        while index < len(nums) and nums[index] < target:
            index += 1
        return index


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    answer = solution.searchInsert(nums=nums, target=target)
    print(answer)
