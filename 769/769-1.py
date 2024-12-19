#! /usr/bin/python pyton

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [4, 3, 2, 1, 0], 1
        ),
        (
            [1, 0, 2, 3, 4], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, expected = example
        got = solution.maxChunksToSorted(
            arr=arr
        )
        assert got == expected, f"Error in samples {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
