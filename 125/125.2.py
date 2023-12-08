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
        return r == list(reversed(r))


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
