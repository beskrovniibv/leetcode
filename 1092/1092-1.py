#! /usr/bin/env python

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ans1, ans2 = [], []
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            while i < len(str1) and str1[i] != str2[j]:
                ans1.append(str1[i])
                i += 1
            while i < len(str1) and str1[i] == str2[j]:
                ans1.append(str1[i])
                i += 1
                j += 1
            while i == len(str1) and j < len(str2):
                ans1.append(str2[j])
                j += 1
        i, j = 0, 0
        while i < len(str2) and j < len(str1):
            while i < len(str2) and str2[i] != str1[j]:
                ans2.append(str2[i])
                i += 1
            while i < len(str2) and str2[i] == str1[j]:
                ans2.append(str2[i])
                i += 1
                j += 1
            while i == len(str2) and j < len(str1):
                ans2.append(str1[j])
                j += 1
        return "".join(ans1) if len(ans1) < len(ans2) else "".join(ans2)


def main():
    examples = (
        # (
        #     "abac", "cab", "cabac"
        # ),
        # (
        #     "aaaaaaaa", "aaaaaaaa", "aaaaaaaa"
        # ),
        (
            "bcacaaab", "bbabaccc", "bbabcacccaaab"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        str1, str2, expected = example
        got = solution.shortestCommonSupersequence(
            str1=str1,
            str2=str2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
