#! usr/bin/python

# 1160. Find Words That Can Be Formed by Characters

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        d_chars = {}
        for char in chars:
            d_chars[char] = d_chars.get(char, 0) + 1
        for word in words:
            d_word = {}
            for char in word:
                d_word[char] = d_word.get(char, 0) + 1
            flag = True
            for key, value in d_word.items():
                c_value = d_chars.get(key, 0)
                if c_value < value:
                    flag = False
                    break
            if flag:
                result += len(word)
        return result


if __name__ == '__main__':
    # case 1
    # words = ['cat', 'bt', 'hat', 'tree']
    # chars = 'atach'
    # case2
    words = ['hello', 'world', 'leetcode']
    chars = 'welldonehoneyr'    

    solution = Solution()
    answer = solution.countCharacters(words, chars)
    print(answer)
