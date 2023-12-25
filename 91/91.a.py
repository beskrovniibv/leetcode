#! usr/bin/python

# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        ll = None
        for i in range(1, n + 1):
            l = ord(s[i - 1]) - ord('0')
            if 1 <= l <= 9:
                dp[i] += dp[i - 1]
            if ll is not None:
                ll = ll*10 + l
                if 10 <= ll <= 26:
                    dp[i] += dp[i - 2]
            ll = l
        return dp[-1]


if __name__ == '__main__':
    # case 1
    # s = '12'
    # case 2
    # s = '226'
    # case 3
    # s = '06'
    # case
    # s = '11106'
    # case
    s = '11111111111111111111111111111111111111111111111111111111111100'

    solution = Solution()
    answer = solution.numDecodings(s)
    print(answer)
