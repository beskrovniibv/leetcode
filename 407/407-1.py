#! /usr/bin/python python python3

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4
        ),
        (
            [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]], 10
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        heightMap, expected = example
        got = solution.trapRainWater(
            heightMap=heightMap
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
