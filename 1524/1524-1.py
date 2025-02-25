#! /usr/bin/env python

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 1
        s = 0
        result = 0
        for e in arr:
            s += e
            if s & 1 == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1
        return result % (int(1e9) + 7)


def main():
    examples = (
        (
            [1, 3, 5], 4
        ),
        (
            [2, 4, 6], 0
        ),
        (
            [1, 2, 3, 4, 5, 6, 7], 16
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, expected = example
        got = solution.numOfSubarrays(
            arr=arr
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
