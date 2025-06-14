#! /usr/bin/env python

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = [c for c in str(num)]
        mx, mn = {}, {}
        for c in s:
            if c != '9':
                mx[c] = '9'
                break
        mn[s[0]] = '0'
        max, min = 0, 0
        for c in s:
            max = max*10 + (int(c) if mx.get(c, None) is None else int(mx[c]))
            min = min*10 + (int(c) if mn.get(c, None) is None else int(mn[c]))
        return max - min


def main():
    examples = (
        (
            11891, 99009
        ),
        (
            90, 99
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        num, expected = example
        got = solution.minMaxDifference(
            num=num
        )
        assert got == expected, f"Error in sample {idx}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
