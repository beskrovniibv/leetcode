#! /usr/bin/env python

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n, l, r = len(blocks), 0, 0
        c, mx = 0, 0
        while r < n:
            if blocks[r] == "B":
                c += 1
            r += 1
            if r - l > k:
                if blocks[l] == "B":
                    c -= 1
                l += 1
            mx = max(mx, c)
            if mx == k:
                return 0
        return k - mx


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
