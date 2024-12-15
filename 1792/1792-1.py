#! /usr/bin/python python

from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pass


def main():
    examples = (
        (
            [[1, 2], [3, 5], [2, 2]], 2, 0.78333
        ),
        (
            [[2, 4], [3, 9], [4, 5], [2, 10]], 4, 0.53485
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        classes, extraStudents, expected = example
        got = solution.maxAverageRatio(
            classes=classes,
            extraStudents=extraStudents
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
