#! usr/bin/python

# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        r, n = 0, x
        while n > 0:
            r = r*10 + n % 10
            n //= 10
        return x == r


if __name__ == '__main__':
    x = int(input())
    solve = Solution()
    print(solve.isPalindrome(x))
