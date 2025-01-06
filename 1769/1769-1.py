#! /usr/bin/python python python3

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, list(boxes)))
        n = len(boxes)
        result = [0]*n
        c = 0
        for i in range(1, n):
            c += boxes[i - 1]
            result[i] = result[i - 1] + c
        c = 0
        s = 0
        for i in range(n - 2, -1, -1):
            c += boxes[i + 1]
            s += c
            result[i] += s
        return result


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
