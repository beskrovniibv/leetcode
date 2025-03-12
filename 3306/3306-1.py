#! /usr/bin/env python

VOWELS = "aeiou"


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        result = 0
        n = len(word)
        c = 0
        v = {}
        vs = set()
        l = 0
        for r in range(n):
            ch = word[r]
            if ch in VOWELS:
                v[ch] = v.get(ch, 0) + 1
                vs.add(ch)
            else:
                c += 1
            if len(vs) == 5 and c == k:
                result += 1
                while True:
                    ch = word[l]
                    if v[ch] > 1:
                        v[ch] = v[ch] - 1
                        result += 1
                        l += 1
                    else:
                        break
                continue
            if c > k:
                while c > k:
                    ch = word[l]
                    if ch in VOWELS:
                        t = v.get(ch, 0)
                        if t == 0:
                            continue
                        if t == 1:
                            vs.remove(ch)
                        v[ch] = t - 1
                    else:
                        c -= 1
                    l += 1
                    if len(vs) == 5 and c == k + 1:
                        result += 1
                if len(vs) == 5 and c == k:
                    result += 1
        while c >= k and l < r:
            ch = word[l]
            if ch in VOWELS:
                t = v.get(ch, 0)
                if t == 0:
                    continue
                if t == 1:
                    vs.remove(ch)
                v[ch] = t - 1
            else:
                c -= 1
            l += 1
            if len(vs) == 5 and c == k:
                result += 1
        return result


def main():
    examples = (
        (
            "aoaiuefi", 1, 4
        ),
        (
            "aadieuoh", 1, 2
        ),
        (
            "akiuboe", 2, 1
        ),
        (
            "buoeia", 0, 1
        ),
        (
            "iqeaouqi", 2, 3
        ),
        (
            "aeioqq", 1, 0
        ),
        (
            "aeiou", 0, 1
        ),
        (
            "ieaouqqieaouqq", 1, 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        word, k, expected = example
        got = solution.countOfSubstrings(
            word=word,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
