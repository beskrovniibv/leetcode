#! /usr/bin/env python

class ProductOfNumbers:

    def __init__(self):
        self.size = 0
        self.array = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.size = 0
            self.array = [1]
            return
        value = self.size and self.array[-1] or 1
        self.array.append(num*value)
        self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.array[-1] // self.array[self.size - k]


def main():
    examples = (
        (
            ["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"], [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]], [None, None, None, None, None, None, 20, 40, 0, None, 32]
        ),
    )
    for idx, example in enumerate(examples):
        commands, args, expected = example
        got = []
        for command in zip(commands, args):
            if command[0] == "ProductOfNumbers":
                solution = ProductOfNumbers()
                got.append(None)
            elif command[0] == "add":
                got.append(solution.add(*command[1]))
            elif command[0] == "getProduct":
                got.append(solution.getProduct(*command[1]))
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
