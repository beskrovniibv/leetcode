#! /usr/bin/python python python3

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        result = 0
        for d in derived:
            result ^= d
        return result == 0


def main():
    examples = (
        (
            [1, 1, 0], True
        ),
        (
            [1, 1], True
        ),
        (
            [1, 0], False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        derived, expected = example
        got = solution.doesValidArrayExist(
            derived=derived
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
