#! /usr/bin/python python

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        partial = 0
        for value in values:
            result = max(result, value + partial)
            partial = max(partial, value) - 1
        return result


def main():
    examples = (
        (
            [8, 1, 5, 2, 6], 11
        ),
        (
            [1, 2], 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        values, expected = example
        got = solution.maxScoreSightseeingPair(
            values=values
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
