#! usr/bin/python

# 203. Remove Linked List Elements

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        node = head
        while True:
            if not node.next:
                return head
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next


if __name__ == '__main__':
    # case 1
    # [1,2,6,3,4,5,6]
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(6)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next.next = ListNode(6)
    # val = 6
    # case 3
    # head = ListNode(7)
    # head.next = ListNode(7)
    # head.next.next = ListNode(7)
    # head.next.next.next = ListNode(7)
    # val = 7
    # case 39
    # [1, 2]
    # val = 2
    head = ListNode(1)
    head.next = ListNode(2)
    val = 2

    solution = Solution()
    solution.removeElements(head, val)
