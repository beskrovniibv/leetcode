#! /usr/bin/python python python3

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pass


def main():
    examples = (
        (
            ["a", "aba", "ababa", "aa"], 4
        ),
        (
            ["pa", "papa", "ma", "mama"], 2
        ),
        (
            ["abab", "ab"], 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        words, expected = example
        got = solution.countPrefixSuffixPairs(
            words=words
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
