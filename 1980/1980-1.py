#! /usr/bin/env python

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        result = ""
        for i in range(n):
            result += ("0", "1")[nums[i][i] == "0"]
        return result


def main():
    examples = (
        (
            ["01", "10"], "11"
        ),
        (
            ["00", "01"], "10"
        ),
        (
            ["111", "011", "001"], "000"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.findDifferentBinaryString(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
