#! /usr/bin/python python python3

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [1, 3, 4, 2], [[1, 4], [2, 3]], 2
        ),
        (
            [2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, mat, expected = example
        got = solution.firstCompleteIndex(
            arr=arr,
            mat=mat,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."



if __name__ == "__main__":
    main()
