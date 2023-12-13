#! usr/bin/python

# 141. Linked List Cycle

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head
        while True:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
