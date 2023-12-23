#! usr/bin/python

# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        while n > 1:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            if s in visited:
                return False
            visited.add(s)
            n = s
        return True


if __name__ == '__main__':
    # case 1
    # n = 19
    # case 2
    n = 2

    solution = Solution()
    answer = solution.isHappy(n)
    print(('false', 'true')[answer])
