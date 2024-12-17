#! /usr/bin/python python

from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        letters = [0]*26
        for ch in s:
            letters[ord(ch) - ord("a")] += 1
        r = len(letters) - 1
        while r >= 0:
            if letters[r] == 0:
                r -= 1
                continue
            result.append(min(repeatLimit, letters[r])*chr(ord("a") + r))
            letters[r] -= min(repeatLimit, letters[r])
            if letters[r] == 0:
                r -= 1
            else:
                l = r - 1
                while l >= 0 and letters[l] == 0:
                    l -= 1
                if l >= 0:
                    result.append(chr(ord("a") + l))
                    letters[l] -= 1
                else:
                    r = l - 1
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
