#! /usr/bin/env python

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        pass


def main():
    examples = (
        (
            "abcdefghi", 3, "x", ["abc", "def", "ghi"]
        ),
        (
            "abcdefghij", 3, "x", ["abc", "def", "ghi", "jxx"]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, k, fill, expected = example
        got = solution.divideString(
            s=s,
            k=k,
            fill=fill,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
