#! /usr/bin/python pyton

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        new = True
        for i in range(n):
            if new:
                left = i
                mn = arr[i]
                mx = arr[i]
                new = False
            else:
                mn = min(mn, arr[i])
                mx = max(mx, arr[i])
            if mn == left and mx == i:
                result += 1
                new = True
        return result


def main():
    examples = (
        (
            [4, 3, 2, 1, 0], 1
        ),
        (
            [1, 0, 2, 3, 4], 4
        ),
        (
            [1, 2, 0, 3], 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, expected = example
        got = solution.maxChunksToSorted(
            arr=arr
        )
        assert got == expected, f"Error in samples {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
