#! /usr/bin/env python

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass


def main():
    examples = (
        (
            "ababcbacadefegdehijhklij", [9, 7, 8]
        ),
        (
            "eccbbbbdec", [10]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.partitionLabels(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
