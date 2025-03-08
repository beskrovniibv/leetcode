#! /usr/bin/env python

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        pass


def main():
    examples = (
        (
            "WBBWWBBWBW", 7, 3
        ),
        (
            "WBWBBBW", 2, 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        blocks, k, expected = example
        got = solution.minimumRecolors(
            blocks=blocks,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
