#! usr/bin/python

# 1688. Count of Matches in Tournament

def count(n: int, r: int = 0) -> int:
    if n == 2:
        return r + 1
    if n & 1 != 1:
        return count(n//2, r + n//2)
    else:
        return count((n - 1)//2 + 1, r + (n - 1)//2)


class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n < 2:
            return 0
        return count(n)


if __name__ == '__main__':
    # case 1
    # n = 7
    # case 2
    n = 14

    solution = Solution()
    answer = solution.numberOfMatches(n)
    print(answer)
