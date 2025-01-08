#! /usr/bin/python python python3

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1
        return result


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
