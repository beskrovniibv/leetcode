#! /usr/bin/env python

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        chars = {}
        for idx, ch in enumerate(s):
            f, l = chars.get(ch, [-1, -1])
            if f == -1:
                f = idx
            l = max(l, idx)
            chars[ch] = [f, l]
        result = []
        end = None
        for i in range(n):
            if end is not None and i > end:
                result.append(i)
                end = None
            c = s[i]
            f, l = chars[c]
            end = max(end and end or l, l)
        if end:
            result.append(end + 1)
        for i in range(len(result) - 1, 0, -1):
            result[i] = result[i] - result[i - 1]
        return result


def main():
    examples = (
        (
            "caedbdedda", [1, 9]
        ),
        (
            "ababcbacadefegdehijhklij", [9, 7, 8]
        ),
        (
            "eccbbbbdec", [10]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.partitionLabels(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
