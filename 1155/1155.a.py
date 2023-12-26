#! usr/bin/python

# 1155. Number of Dice Rolls With Target Sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for d in range(1, n + 1):
            for f in range(1, k + 1):
                for k in range(target, f - 1, -1):
                    if dp[d - 1][k - f] != 0:
                        s = (dp[d][k] + dp[d - 1][k - f]) % mod
                        dp[d][k] = s
        return dp[d][target]


if __name__ == '__main__':
    # case 1
    # n, k, target = 1, 6, 3
    # case 2
    n, k, target = 2, 6, 7
    # case 3
    # n, k, target = 30, 30, 500

    solution = Solution()
    answer = solution.numRollsToTarget(n, k, target)
    print(answer)
