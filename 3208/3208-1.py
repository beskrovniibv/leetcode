#! /usr/bin/env python

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        pass


def main():
    examples = (
        (
            [0, 1, 0, 1, 0], 3, 3
        ),
        (
            [0, 1, 0, 0, 1, 0, 1], 6, 2
        ),
        (
            [1, 1, 0, 1], 4, 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        colors, k, expected = example
        got = solution.numberOfAlternatingGroups(
            colors=colors,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
