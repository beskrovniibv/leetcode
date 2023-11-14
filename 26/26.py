#! usr/bin/python

# 26. Remove Duplicates from Sorted Array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, skip = 0, 0
        queue = []
        for i, num in enumerate(nums):
            if len(queue) == 0:
                queue.append(num)
                index += 1
            elif queue[-1] != num:
                queue.append(num)
                nums[index] = num
                index += 1
            else:
                skip += 1
        return index


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    solution = Solution()
    answer = solution.removeDuplicates(nums)
    print(f'{answer}:', end=' ')
    print(*nums)
