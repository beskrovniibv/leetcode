#! /usr/bin/python python

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        special = [0]*n
        result = []
        s = 0
        for i in range(1, n):
            if nums[i] & 1 == nums[i - 1] & 1:
                s += 1
            special[i] = s
        for q in queries:
            result.append(special[q[0]] == special[q[1]])
        return result


def main():
    examples = (
        (
            [3, 4, 1, 2, 6], [[0, 4]], [False]
        ),
        (
            [4, 3, 1, 6], [[0, 2], [2, 3]], [False, True]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, queries, expected = example
        got = solution.isArraySpecial(
            nums=nums,
            queries=queries
        )
        assert got == expected, f"Error in sample: {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
