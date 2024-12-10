#! /usr/bin/python python

class Solution:
    def maximumLength(self, s: str) -> int:
        pass


def main():
    examples = (
        ("aaaa", 2),
        ("abcdef", -1),
        ("abcaba", 1)
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
