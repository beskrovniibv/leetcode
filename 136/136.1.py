#! usr/bin/python

# 136. Single Number

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    # case 1
    nums = [2, 2, 1]

    solution = Solution()
    print(solution.singleNumber(nums))
