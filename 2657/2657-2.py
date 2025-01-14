#! /usr/bin/python python python3

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0]*n
        a, b = set(), set()
        c = 0
        for i in range(n):
            a.add(A[i])
            b.add(B[i])
            if A[i] == B[i]:
                c += 1
                result[i] = c
                continue
            if A[i] in b:
                c += 1
            if B[i] in a:
                c += 1
            result[i] += c
        return result


def main():
    examples = (
        (
            [1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4]
        ),
        (
            [2, 3, 1], [3, 1, 2], [0, 1, 3]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        A, B, expected = example
        got = solution.findThePrefixCommonArray(
            A=A,
            B=B
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
