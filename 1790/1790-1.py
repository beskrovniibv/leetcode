#! /usr/bin/env python

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        c, idx1, idx2 = 0, -1, -1
        for i in range(n):
            if s1[i] != s2[i]:
                c += 1
                if c > 2:
                    return False
                if c == 1:
                    idx1 = i
                else:
                    idx2 = i
        return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]


def main():
    examples = (
        (
            "npv", "zpn", False
        ),
        (
            "bank", "kanb", True
        ),
        (
            "attack", "defend", False
        ),
        (
            "kelb", "kelb", True
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s1, s2, expected = example
        got = solution.areAlmostEqual(
            s1=s1,
            s2=s2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
