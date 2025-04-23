#! /usr/bin/env python

class Solution:
    def countLargestGroup(self, n: int) -> int:
        pass

def main():
    examples = (
        (
            13, 4
        ),
        (
            2, 2
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.countLargestGroup(
            n=n
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
