#! /usr/bin/python python python3

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wc1 = [{} for word in words1]
        wc2 = {}
        for i, word in enumerate(words1):
            for c in word:
                wc1[i][c] = wc1[i].get(c, 0) + 1
        for word in words2:
            t = {}
            for c in word:
                t[c] = t.get(c, 0) + 1
            for key, value in t.items():
                wc2[key] = max(wc2.get(key, 0), value)
        result = [0]*len(words1)
        for i in range(len(words1)):
            for key, value in wc2.items():
                if wc1[i].get(key, 0) >= value:
                    continue
                else:
                    break
            else:
                result[i] += 1
        return [word for i, word in enumerate(words1) if result[i] == 1]


def main():
    examples = (
        # (
        #     ["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"], ["facebook", "google", "leetcode"]
        # ),
        # (
        #     ["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"], ["apple", "google", "leetcode"]
        # ),
        # (
        #     ["amazon","apple","facebook","google","leetcode"], ["e","oo"], ["facebook", "google"]
        # ),
        (
            ["amazon","apple","facebook","google","leetcode"], ["oc","ec","ceo"], ["facebook", "leetcode"]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        wosrd1, words2, expected = example
        got = solution.wordSubsets(
            words1=wosrd1,
            words2=words2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
