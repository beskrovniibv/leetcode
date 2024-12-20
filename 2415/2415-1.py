# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode], isOddLevel: bool) -> None:
            if not left:
                return
            if isOddLevel:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, not isOddLevel)
            dfs(left.right, right.left, not isOddLevel)

        dfs(root.left, root.right, True)
        return root


def getTreeFromList(treeList: List[int]) -> TreeNode:
    pass


def getListFromTree(root: TreeNode) -> List[int]:
    pass


def main():
    examples = (
        (
            [2, 3, 5, 8, 13, 21, 34], [2, 5, 3, 8, 13, 21, 34]
        ),
        (
            [7, 13, 11], [7, 11, 13]
        ),
        (
            [0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        treeList, expected = example
        root = getTreeFromList(treeList)
        got = solution.reverseOddLevels(root)
        answer = getListFromTree(got)
        assert answer == expected, f"Error in sample {idx + 1}, expected {expected}, got {answer}"


if __name__ == "__main__":
    main()
    