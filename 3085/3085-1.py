#! /usr/bin/env python

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = {}
        for c in word:
            d[c] = d.get(c, 0) + 1
        a = list(d.values())
        result = len(word)
        for i in range(len(a)):
            deleted = 0
            for j in range(len(a)):
                if a[i] > a[j]:
                    deleted += a[j]
                elif a[j] > a[i] + k:
                    deleted += a[j] - (a[i] + k)
            result = min(result, deleted)
        return result


def main():
    examples = (    
        (
            "aabcaba", 0, 3
        ),
        (
            "dabdcbdcdcd", 2, 2
        ),
        (
            "aaabaaa", 2, 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        word, k, expected = example
        got = solution.minimumDeletions(
            word=word,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
