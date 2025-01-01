#! /usr/bin/python python python3

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        psumz = [0] + [0]*n
        psumo = [0] + [0]*n
        for i in range(1, n + 1):
            psumz[i] = psumz[i - 1] + (1 if s[i - 1] == "0" else 0)
            psumo[i] = psumo[i - 1] + (1 if s[i - 1] == "1" else 0)
        result = 0
        for i in range(n - 1):
            ans0 = psumz[i + 1] - psumz[0]
            ans1 = psumo[n] - psumo[i + 1]
            result = max(result, ans0 + ans1)
        return result


def main():
    examples = (
        (
            "011101", 5
        ),
        (
            "00111", 5
        ),
        (
            "1111", 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.maxScore(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
