#! /usr/bin/env python

class Solution:
    def count(self, n):
        if n == 1:
            return 1
        return 2*n + 2*(n - 2) + self.count(n - 1)

    def coloredCells(self, n: int) -> int:
        return self.count(n)


def main():
    examples = (
        (
            1, 1
        ),
        (
            2, 5
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.coloredCells(
            n=n
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
