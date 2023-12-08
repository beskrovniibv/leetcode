#! usr/bin/python

# 125. Valid Palindrome

from string import ascii_letters, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        for c in s:
            if c not in ascii_letters + digits:
                s = s.replace(c, '')
        return s.replace(' ', '').lower() == s.replace(' ', '').lower()[::-1]


if __name__ == '__main__':
    # case 1
    # s = 'A man, a plan, a canal: Panama'
    # case 2
    # s = 'race a car'
    # case 3
    # s = ' '
    # case 4
    s = '1P1'

    solution = Solution()
    answer = ('false', 'true')[solution.isPalindrome(s)]
    print(answer)
