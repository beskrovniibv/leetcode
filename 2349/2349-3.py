MAX_SIZE = int(1e9)
BLOCK_SIZE = int(10_000)
BLOCK_COUNT = (MAX_SIZE + 1) // BLOCK_SIZE


class NumberContainers:

    def __init__(self):
        self.indices = {}  # [-1]*MAX_SIZE
        self.blocks = [{} for _ in range(BLOCK_COUNT + 1)]
        self.blocks_idx = {}

    def change(self, index: int, number: int) -> None:
        old_number = self.indices.get(index, -1)
        if old_number != -1:
            self.blocks[index // BLOCK_SIZE][old_number] -= 1
        block = index // BLOCK_SIZE
        self.blocks[block][number] = self.blocks[block].get(number, 0) + 1
        self.indices[index] = number
        if not self.blocks_idx.get(block):
            self.blocks_idx[block] = {}
        self.blocks_idx[block][index] = number

    def find(self, number: int) -> int:
        for i, block in enumerate(self.blocks):
            found = block.get(number)
            if found:
                result = MAX_SIZE
                for k, v in self.blocks_idx[i].items():
                    if v == number:
                        result = min(result, k)
                return result
        return -1


def main():
    examples = (
        (
            ["NumberContainers", "find", "change", "find"],  [[], [10], [1000000000, 10], [10]],  None
        ),
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
