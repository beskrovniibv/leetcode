#! /usr/bin/python python python3

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pass


def main():
    examples = (
        (
            "110", [1, 1, 3]
        ),
        (
            "001011", [11, 8, 5, 4, 3, 4]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        boxes, expected = example
        got = solution.minOperations(
            boxes=boxes
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
