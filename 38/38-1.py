#! /usr/bin/env python

class Solution:
    def countAndSay(self, n: int) -> str:
        for i in range(1, n + 1):
            if i == 1:
                rle = "1"
            else:
                l = None
                c = 0
                temp = []
                for ch in rle:
                    if l and ch == l:
                        c += 1
                    elif not l:
                        l = ch
                        c = 1
                    else:
                        temp.append(f"{c}{l}")
                        l = ch
                        c = 1
                temp.append(f"{c}{l}")
                result = "".join(temp)
                rle = result
        return rle


def main():
    examples = (
        (
            4, "1211"
        ),
        (
            1, "1"
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.countAndSay(
            n=n
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
