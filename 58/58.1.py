#! usr/bin/path

# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


if __name__ == '__main__':
    s = input()
    solution = Solution()
    answer = solution.lengthOfLastWord(s)
    print(answer)
