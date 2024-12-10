#! /usr/bin/python python

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s) - 2
        for l in range(n, 0, -1):
            for i1 in range(len(s) - l - 1):
                for i2 in range(i1 + 1, len(s)):
                    for i3 in range(i2 + 1, len(s) - l + 1):
                        if s[i1:i1 + l] == s[i2:i2 + l] == s[i3:i3 + l] and len(set(s[i1:i1 + l])) == 1:
                            return l
        return -1


def main():
    examples = (
        ("aaaa", 2),
        ("abcdef", -1),
        ("abcaba", 1),
        ("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde", 2)
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.maximumLength(
            s=s
        )
        assert got == expected, f"Error in sample: {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
