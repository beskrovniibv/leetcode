#! usr/bin/python

# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        f = True
        for c in strs[0]:
            for i in range(1, len(strs)):
                if not strs[i].startswith(ans + c):
                    f = False
                    break
            else:
                ans += c
            if not f:
                break
        return ans


if __name__ == '__main__':
    array = list(input().split())
    solution = Solution()
    print(solution.longestCommonPrefix(array))
