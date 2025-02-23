#! /usr/bin/env python

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        l = f"{self.left.val}" if self.left else "None"
        r = f"{self.right.val}" if self.right else "None"
        return f"({self.val}: ({l}), ({r}))"


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        st = []
        j = 0
        for val in preorder:
            node = TreeNode(val)
            if st:
                if not st[-1].left:
                    st[-1].left = node
                else:
                    st[-1].right = node
            st.append(node)
            while len(st) > 1 and st[-1].val == postorder[j]:
                st.pop()
                j += 1
        return st[0]


def main():
    solution = Solution()
    solution.constructFromPrePost(
        postorder=[4, 5, 2, 6, 7, 3, 1],
        preorder=[1, 2, 4, 5, 3, 6, 7]
    )


if __name__ == "__main__":
    main()
