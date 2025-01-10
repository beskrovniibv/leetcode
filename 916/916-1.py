#! /usr/bin/python python python3

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        pass


def main():
    examples = (
        (
            ["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"], ["facebook", "google", "leetcode"]
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"], ["apple", "google", "leetcode"]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        wosrd1, words2, expected = example
        got = solution.wordSubsets(
            words1=wosrd1,
            words2=words2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
