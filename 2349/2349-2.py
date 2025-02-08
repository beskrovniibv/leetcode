class NumberContainers:

    def __init__(self):
        self.indices = {}
        self.numbers = {}
        self.mins = {}

    def change(self, index: int, number: int) -> None:
        old = self.indices.get(index)
        if old:
            self.numbers[old].remove(index)
        l = self.numbers.get(number, set())
        l.add(index)
        self.numbers[number] = l
        self.indices[index] = number

    def find(self, number: int) -> int:
        index = self.numbers.get(number)
        return index and min(index) or -1


def main():
    examples = (
        (
            ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"], [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]], [None, -1, None, None, None, None, 1, None, 2]
        ),
    )
    for idx, example in enumerate(examples):
        cmds, args, expected = example
        got = []
        for cmd, arg in zip(cmds, args):
            if cmd == "NumberContainers":
                numbercontainers = NumberContainers()
                got.append(None)
            elif cmd == "find":
                got.append(numbercontainers.find(*arg))
            elif cmd == "change":
                numbercontainers.change(*arg)
                got.append(None)
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."

if __name__ == "__main__":
    main()
