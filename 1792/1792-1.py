#! /usr/bin/python python

from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        result = 0
        for k in range(extraStudents):
            classes.sort(key=lambda _class: (_class[0] + 1)/(_class[1] + 1) - (_class[0])/(_class[1]))
            classes[-1][0] += 1
            classes[-1][1] += 1
        for k in classes:
            result += k[0]/k[1]
        return result/len(classes)


def main():
    examples = (
        (
            [[1, 2], [3, 5], [2, 2]], 2, 0.78333
        ),
        (
            [[2, 4], [3, 9], [4, 5], [2, 10]], 4, 0.53485
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        classes, extraStudents, expected = example
        got = solution.maxAverageRatio(
            classes=classes,
            extraStudents=extraStudents
        )
        assert abs(got - expected) < 10e5, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
