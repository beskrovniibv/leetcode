#! /usr/bin/python python python3

class Solution:
    def minimumLength(self, s: str) -> int:
        pass


def main():
    examples = (
        (
            "abaacbcbb", 5
        ),
        (
            "aa", 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.minimumLength(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
