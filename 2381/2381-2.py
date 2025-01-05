#! /usr/bin/python python python3

from string import ascii_lowercase
from typing import List


class Solution:
    def shift(self, s: str, shifts: List[int]) -> str:
        abc = list(ascii_lowercase)
        result = list(s)
        for i, sh in enumerate(shifts):
            result[i] = abc[(ord(result[i]) + sh - ord("a")) % len(abc)]
        return ''.join(result)

    def shiftingLetters(self,  s: str,  shifts: List[List[int]]) -> str:
        n = len(s)
        total = [0]*(n + 1)
        for shift in shifts:
            l, r, d = shift
            total[l] = total[l] + (+1 if d == 1 else -1)
            total[r + 1] = total[r + 1] + (-1 if d == 1 else +1)
        total = [0] + total
        for i in range(1, n + 1):
            total[i] = total[i - 1] + total[i]
        return self.shift(s, total[1:-1])


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
