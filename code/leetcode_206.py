from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre, cur, nex = head, head, head.next
        while nex is not None:
            if cur == head:
                cur.next = None
            pre = cur
            cur = nex
            nex = nex.next
            cur.next = pre
        return cur

head = [1,2,3,4,5]
solution = Solution()
solution.reverseList(head)