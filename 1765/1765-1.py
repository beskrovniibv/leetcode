#! /usr/bin/python python python3

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        pass


def main():
    examples = (
        (
            [[0, 1], [0, 0]], [[1, 0], [2, 1]]
        ),
        (
            [[0, 0, 1], [1, 0, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        isWater, expected = example
        got = solution.highestPeak(
            isWater=isWater
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
