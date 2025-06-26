#! /usr/bin/env python

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        pass


def main():
    examples = (
        (
            "1001010", 5, 5
        ),
        (
            "00101001", 1, 6
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, k, expected = example
        got = solution.longestSubsequence(
            s=s,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
