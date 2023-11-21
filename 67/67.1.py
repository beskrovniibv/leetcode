#! usr/bin/path

# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        binary_a = [0] * (maxlen - len(a)) + list(map(int, a))
        binary_b = [0] * (maxlen - len(b)) + list(map(int, b))
        carry = 0
        result = []
        for i in range(maxlen - 1, -1, -1):
            partial = binary_a[i] + binary_b[i] + carry
            result.append(partial % 2)
            carry = partial // 2
        if carry:
            result.append(carry)
        return ''.join(map(str, reversed(result)))


if __name__ == '__main__':
    a, b = input().split()
    solution = Solution()
    answer = solution.addBinary(a, b)
    print(answer)
