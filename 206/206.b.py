#! usr/bin/python

# 206. Reverse Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        while head is not None:
            node = head
            head = head.next
            node.next = result
            result = node
        return result


if __name__ == '__main__':
    # case 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    solution.reverseList(head)
