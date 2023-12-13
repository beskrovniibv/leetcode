#! usr/bin/python

# 1464. Maximum Product of Two Elements in an Array

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1, mx2 = max(nums[0], nums[1]), min(nums[0], nums[1])
        r = mx1*mx2
        for i in range(2, len(nums)):
            n = nums[i]
            if mx1*n >= r:
                if n > mx1:
                    mx2 = mx1
                    mx1 = n
                else:
                    mx2 = n
                r = mx1*mx2
        return (mx1 - 1)*(mx2 - 1)


if __name__ == '__main__':
    # case 1
    # nums = [10, 2, 5, 2]
    # case 2
    nums = [1, 9, 4, 8, 8, 9, 4, 6]

    solution = Solution()
    answer = solution.maxProduct(nums)
    print(answer)
