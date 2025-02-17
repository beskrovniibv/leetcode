#! /usr/bin/env python

import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        for l in range(1, len(tiles) + 1):
            s = set()
            for p in itertools.permutations(tiles, l):
                s.add(p)
            result += len(s)
        return result


def main():
    examples = (
        (
            "AAB", 8
        ),
        (
            "AAABBC", 188
        ),
        (
            "V", 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        tiles, expected = example
        got = solution.numTilePossibilities(
            tiles=tiles
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
