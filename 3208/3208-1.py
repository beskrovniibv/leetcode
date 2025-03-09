#! /usr/bin/env python

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        result = 0
        n = len(colors)
        prv = colors[0]
        cur_len = 1
        for i in range(1, n + k - 1):
            idx = i % n
            nxt = colors[idx]
            if nxt == prv:
                cur_len = 1
                prv = nxt
                continue
            cur_len += 1
            if cur_len >= k:
                result += 1
            prv = nxt
        return result


def main():
    examples = (
        (
            [0, 1, 0, 1, 0], 3, 3
        ),
        (
            [0, 1, 0, 0, 1, 0, 1], 6, 2
        ),
        (
            [1, 1, 0, 1], 4, 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        colors, k, expected = example
        got = solution.numberOfAlternatingGroups(
            colors=colors,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
