#! /usr/bin/env python

class Solution:
    def robotWithString(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        result = []
        stack = []
        mn = 'a'
        for c in s:
            d[c] -= 1
            while mn < "z" and d.get(mn, 0) == 0:
                mn = chr(ord(mn) + 1)
            stack.append(c)
            while stack and stack[-1] <= mn:
                result.append(stack.pop())
        return ''.join(result)


def main():
    examples = (
        (
            "zza", "azz"
        ),
        (
            "bac", "abc"
        ),
        (
            "bdda", "addb"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.robotWithString(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
