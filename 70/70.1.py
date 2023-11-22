#! usr/bin/python

# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * max(n + 1, 3)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    n = int(input())
    solution = Solution()
    answer = solution.climbStairs(n)
    print(answer)
