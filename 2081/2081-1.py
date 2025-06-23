#! /usr/bin/env python

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        pass


def main():
    examples = (
        (
            2, 5, 25
        ),
        (
            3, 7, 499
        ),
        (
            7, 17, 20379000
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        k, n, expected = example
        got = solution.kMirror(
            k=k,
            n=n,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
