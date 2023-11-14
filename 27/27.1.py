#! usr/bin/python

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        skip = 0
        k = 0
        for i, num in enumerate(nums):
            if num == val:
                skip += 1
            else:
                nums[i - skip] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    val = int(input())
    nums = list(map(int, input().split()))
    solution = Solution()
    k = solution.removeElement(nums, val)
    print(f'{k}: ', end=' ')
    print(*nums)
