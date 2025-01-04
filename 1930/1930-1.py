#! /usr/bin/python python python3

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = [[len(s), -1, 0]]*26
        for i, c in enumerate(s):
            ch = ord(c) - ord("a")
            chars[ch] = [min(i, chars[ch][0]), max(i, chars[ch][1]), 0]
        for i in range(26):
            b, e, _ = chars[i]
            c = set()
            for j in range(b + 1, e):
                c.add(s[j])
            chars[i][2] = len(c)
        result = 0
        for i in range(26):
            b, e, c = chars[i]
            if e > b:
                result += c
        return result


def main():
    examples = (
        (
            "abcacba", 6
        ),
        (
            "aabca", 3
        ),
        (
            "adc", 0
        ),
        (
            "bbcbaba", 4
        ),
        (
            "ckafnafqo", 4
        ),
        (
            "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp", 161
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.countPalindromicSubsequence(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."



if __name__ == "__main__":
    main()


"""
tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp
"""