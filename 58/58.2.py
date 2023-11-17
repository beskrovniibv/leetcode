#! usr/bin/path

# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v = ' ' + s.strip()
        index = len(v) - 1
        end, start = 0, 0
        if index > 0:
            end = index
            while index > 0 and v[index] != ' ':
                index -= 1
            start = index
        return end - start


if __name__ == '__main__':
    s = input()
    solution = Solution()
    answer = solution.lengthOfLastWord(s)
    print(answer)
