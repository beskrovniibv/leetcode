#! /usr/bin/python python python3

from typing import List


class Solution:
    def shiftingLetters(self,  s: str,  shifts: List[List[int]]) -> str:
        pass


def main():
    examples = (
        (
            "abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace"
        ),
        (
            "dztz",  [[0,  0,  0],  [1,  1,  1]],  "catz"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, shifts, expected = example
        got = solution.shiftingLetters(
            s=s,
            shifts=shifts
        )
        assert got == expected, f"Error in {idx + 1} sample: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
