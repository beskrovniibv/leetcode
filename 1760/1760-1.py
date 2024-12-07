#! /usr/bin/python python

from typing import List


class Solution:
    def countOperations(self, nums: List[int], penalty: int) -> int:
        operations = 0
        for num in nums:
            operations += (num - 1) // penalty
        return operations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            m = (l + r) // 2
            if self.countOperations(nums, m) <= maxOperations:
                r = m
            else:
                l = m + 1
        return l


def main():
    solution = Solution()
    examples = (
        (
            [9], 2, 3
        ),
        (
            [2, 4, 8, 2], 4, 2
        )
    )
    for idx, example in enumerate(examples):
        nums, maxOperation, expected = example
        got = solution.minimumSize(
            nums=nums,
            maxOperations=maxOperation
        )
        assert got == expected, f"Error in {idx + 1} sample: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
