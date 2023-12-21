#! usr/bin/python

# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            r = n % 2
            result *= 2
            result += r
            n //= 2
        return result


if __name__ == '__main__':
    # case 1
    n = 0b00000010100101000001111010011100
    # case 2
    # n = 0b11111111111111111111111111111101
    # case 3
    # n = 0b00011100

    solution = Solution()
    answer = solution.reverseBits(n)
    print(answer)
