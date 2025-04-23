#! /usr/bin/env python

def _sum(v):
    result = 0
    while v:
        result += v%10
        v //= 10
    return result


class Solution:
    def countLargestGroup(self, n: int) -> int:
        result = {}
        _s = {}
        for i in range(1, n + 1):
            s = _sum(i)
            _s[s] = _s.get(s, [])
            _s[s].append(i)
            l = len(_s[s])
            result[l] = result.get(l, 0) + 1
            if l > 1:
                result[l - 1] -= 1
        mx, cmx = None, 0
        for k in result:
            if mx is None:
                mx, cmx = k, result[k]
            elif k > mx:
                mx, cmx = k, result[k]
            else:
                cmx += result[k]
        return cmx


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
