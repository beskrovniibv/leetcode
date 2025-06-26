#! /usr/bin/env python

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        v = int(s, 2)
        if v <= k:
            return n
        c = 0
        q = 2**(n - 1)
        l = 0
        while v > k:
            if s[l] == "1":
                v -= q
                c += 1
            l += 1
            q >>= 1
        return n - c


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
