#! /usr/bin/env python

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, 2, 3, 4, 5, 6, 7, 8], 5
        ),
        (
            [1, 3, 7, 11, 12, 14, 18], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, expected = example
        got = solution.lenLongestFibSubseq(
            arr=arr
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
