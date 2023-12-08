#! usr/bin/python

# 125. Valid Palindrome

from string import ascii_letters, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []
        for i, c in enumerate(s):
            c = c.lower()
            if c in ascii_letters + digits:
                r.append(c)
        for i in range((len(r) + 2 - 1) // 2):
            if r[i] != r[len(r) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    # case 1
    s = 'A man, a plan, a canal: Panama'
    # case 2
    # s = 'race a car'
    # case 3
    # s = ' '
    # case 4
    # s = '1P1'

    solution = Solution()
    answer = ('false', 'true')[solution.isPalindrome(s)]
    print(answer)
