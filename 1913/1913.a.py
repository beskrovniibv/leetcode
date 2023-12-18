#! usr/bin/python

# 1913. Maximum Product Difference Between Two Pairs

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx_mx, mn_mx, mx_mn, mn_mn = sorted(nums[:4], reverse=True)
        for i in range(4, len(nums)):
            num = nums[i]
            if num > mx_mx:
                mn_mx = mx_mx
                mx_mx = num
            elif num > mn_mx:
                mn_mx = num
            elif num < mn_mn:
                mx_mn = mn_mn
                mn_mn = num
            elif num < mx_mn:
                mx_mn = num
        return (mx_mx*mn_mx) - (mx_mn*mn_mn)


if __name__ == '__main__':
    # case 1
    # nums = [5, 6, 2, 7, 4]
    # case 2
    nums = [4, 2, 5, 9, 7, 4, 8]

    solution = Solution()
    answer = solution.maxProductDifference(nums)
    print(answer)
