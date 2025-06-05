#! /usr/bin/env python

from string import ascii_lowercase


class Solution:
    def find(self, array, value):
        if array[ord(value) - ord('a')] != value:
            array[ord(value) - ord('a')] = self.find(array, array[ord(value) - ord('a')])
        return array[ord(value) - ord('a')]

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(baseStr)
        m = len(s1)
        r = ['']*n
        letters = [c for c in ascii_lowercase]
        for i in range(m):
            c1, c2 = s1[i], s2[i]
            c1_l = self.find(array=letters, value=c1)
            c2_l = self.find(array=letters, value=c2)
            if c1_l < c2_l:
                letters[ord(c2_l) - ord('a')] = c1_l
            else:
                letters[ord(c1_l) - ord('a')] = c2_l
        for i in range(n):
            r[i] = self.find(array=letters, value=baseStr[i])
        return ''.join(r)


def main():
    examples = (
        (
            "parker", "morris", "parser", "makkek"
        ),
        (
            "hello", "world", "hold", "hdld"
        ),
        (
            "leetcode", "programs", "sourcecode", "aauaaaaada"
        ),
        (
            "bbbaacaaaaccccbacbbaaccccacbbbccbcbabbbcbcbcaaacac", "aabbccbccabcaccbacabcbccaaaaaaccbbabaabbbbabbabaca", "dwbyvrkacqglybdviivynguhfrlffpkcnoeijzddqhbxxeoefz", "dwayvrkaaqglyadviivynguhfrlffpkanoeijzddqhaxxeoefz"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s1, s2, baseStr, expected = example
        got = solution.smallestEquivalentString(
            s1=s1,
            s2=s2,
            baseStr=baseStr
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
