#! /usr/bin/env python

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        total = set(arr)
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                pr = 2
                p1 = arr[i]
                p2 = arr[j]
                while p1 + p2 in total:
                    pr += 1
                    p1, p2 = p2, p1 + p2
                if pr > 2:
                    result = max(result, pr)
        return result


def main():
    examples = (
        (
            [1, 2, 3, 4, 5, 6, 7, 8], 5
        ),
        (
            [1, 3, 7, 11, 12, 14, 18], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, expected = example
        got = solution.lenLongestFibSubseq(
            arr=arr
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
