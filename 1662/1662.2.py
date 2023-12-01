#! usr/bin/python

# 1662. Check If Two String Arrays are Equivalent

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = ''.join(word1)
        word2 = ''.join(word2)
        return word1 == word2


if __name__ == '__main__':
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddef"]
    solution = Solution()
    print(('no', 'yes')[solution.arrayStringsAreEqual(word1, word2)])
