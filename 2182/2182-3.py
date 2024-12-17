#! /usr/bin/python python

from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        letters = {}
        for ch in s:
            letters[ch] = letters.get(ch, 0) + 1
        for c in 'zyxwvutsrqponmlkjihgfedcba':
            if letters.get(c, 0):
                count = min(letters.get(c), repeatLimit)
                result.append(c*count)
                letters[c] -= count
        print(letters)
        return "".join(result)


def main():
    examples = (
        (
            "cczazcc", 3, "zzcccac"
        ),
        (
            "aababab", 2, "bbabaa"
        ),
        (
            "robnsdvpuxbapuqgopqvxdrchivlifeepy", 2, "yxxvvuvusrrqqppopponliihgfeeddcbba"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, repeatLimit, expected = example
        got = solution.repeatLimitedString(
            s=s,
            repeatLimit=repeatLimit
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
