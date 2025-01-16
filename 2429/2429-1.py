#! /usr/bin/python python python3

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = bin(num2).count('1')
        num1_b = bin(num1)
        result_b = ["0"]*len(num1_b[2:])
        for i, c in enumerate(num1_b[2:]):
            if c == "1":
                result_b[i] = "1"
                n -= 1
            else:
                result_b[i] = "0"
            if n == 0:
                break
        for i in range(len(result_b) - 1, -1, -1):
            if n == 0:
                break
            if result_b[i] == "0":
                result_b[i] = "1"
                n -= 1
        result_b = ["1"]*n + result_b
        result = int("".join(result_b), 2)
        return result


def main():
    examples = (
        (
            25, 72, 24
        ),
        (
            3, 5, 3
        ),
        (
            1, 12, 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        num1, num2, expected = example
        got = solution.minimizeXor(
            num1=num1,
            num2=num2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
