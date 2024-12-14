#! /usr/bin/python python

from typing import List
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        slices = []
        n = len(nums)
        l = 0
        mins = deque([(nums[l], l)])
        maxs = deque([(nums[l], l)])
        w = deque([nums[l]])
        for r in range(1, n):
            num = nums[r]
            w.append(num)
            if abs(mins[0][0] - num) > 2 or abs(maxs[0][0] - num) > 2:
                slices.append((l, r - 1))
                while (mins and abs(mins[0][0] - num) > 2) or (maxs and abs(maxs[0][0] - num) > 2):
                    if l == mins[0][1]:
                        mins.popleft()
                    if l == maxs[0][1]:
                        maxs.popleft()
                    l += 1
                    w.popleft()
            if mins and mins[-1][0] > num:
                mins.pop()
            if maxs and maxs[-1][0] < num:
                maxs.pop()
            mins.append((num, r))
            maxs.append((num, r))
        slices.append((l, r))
        oe = None
        for slice in slices:
            b, e = slice
            # b = max(oe or b - 1, b - 1) + 1
            l = e - b + 1
            result += (l * (l + 1))//2
            if oe:
                i = e - oe
                # if i > 0:
                #     result -= i*(i - 1)//2
                if b > oe:
                    oe = e
            else:
                oe = e
        return result


def main():
    examples = (
        # (
        #     [5, 4, 2, 4], 8
        # ),
        # (
        #     [1, 2, 3], 6
        # ),
        # (
        #     [3, 1, 3, 5, 1, 3], 11
        # ),
        (
            [12, 13, 14, 13, 12, 11, 10, 10, 12, 11, 10, 11, 9, 14], 56
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.continuousSubarrays(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
