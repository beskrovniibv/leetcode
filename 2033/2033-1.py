#! /usr/bin/env python

from math import gcd
from typing import List


def gcd2list(seq):
    result = None
    for e in seq:
        result = result and gcd(result, e) or e
    return result


class Solution:
    def minOperations(self,  grid: List[List[int]],  x: int) -> int:
        seq = sorted([e for line in grid for e in line])
        n = len(seq)
        med = seq[n//2]
        if len(seq) == 1:
            return 0
        m1, m = None, None
        result = 0
        for i, e in enumerate(seq):
            m = e % x
            if m1 and m1 != m:
                return -1
            m1 = m
            result += abs(e - med)//x
        return result


def main():
    examples = (
        (
            [[529, 529, 989], [989, 529, 345], [989, 805, 69]], 92, 25
        ),
        (
            [[931, 128], [639, 712]], 73, 12
        ),
        (
            [[146]], 86, 0
        ),
        (
            [[2, 4], [6, 8]], 2, 4
        ),
        (
            [[1, 5], [2, 3]], 1, 5
        ),
        (
            [[1, 2], [3, 4]], 2, -1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, x, expected = example
        got = solution.minOperations(
            grid=grid,
            x=x
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
