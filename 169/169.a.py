#! usr/bin/python

# 169. Majority Element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        last = 0
        count = 0
        for num in nums:
            if num == last:
                count += 1
            elif count > 0:
                count -= 1
            elif count == 0:
                last = num
                count = 1
        return last


if __name__ == '__main__':
    # case 1
    nums = [3, 2, 3]
    # case 2
    # nums = [2, 2, 1, 1, 1, 2, 2]

    solution = Solution()
    answer = solution.majorityElement(nums)
    print(answer)
