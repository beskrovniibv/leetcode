#! /usr/bin/python python python3

from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [2, 2, 1, 2], 3
        ),
        (
            [1, 2, 0], 3
        ),
        (
            [3, 0, 1, 4, 1], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        favorite, expected = example
        got = solution.maximumInvitations(
            favorite=favorite
        )
        assert got == expected, f"Error in sample {idx+ 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
