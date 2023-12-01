#! usr/bin/python

# 1662. Check If Two String Arrays are Equivalent

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if not word1 and not word2:
            return True
        if not word1 or not word2:
            return False
        i, j = 0, 0
        for part in word1:
            for c in part:
                if i == len(word2):
                    return False
                if c == word2[i][j]:
                    j += 1
                    if j == len(word2[i]):
                        i += 1
                        j = 0
                else:
                    return False
        return i == len(word2) and j == 0


if __name__ == '__main__':
    word1 = ["abc","d","defg"]
    word2 = ["abcddef"]
    solution = Solution()
    print(('no', 'yes')[solution.arrayStringsAreEqual(word1, word2)])
