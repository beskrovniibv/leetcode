#! /usr/bin/env python

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        pass


def main():
    examples = (
        (
            1, 3, "c"
        ),
        (
            1, 4, ""
        ),
        (
            3, 9, "cab"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, k, expected = example
        got = solution.getHappyString(
            n=n,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
