#! /usr/bin/python python python3

class Solution:
    def minimumLength(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        result = 0
        for k, v in counter.items():
            if v < 3:
                result += v
            elif v & 1 == 1:
                result += 1
            else:
                result += 2
        return result


def main():
    examples = (
        (
            "abaacbcbb", 5
        ),
        (
            "aa", 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.minimumLength(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
