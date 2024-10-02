from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        p_del = stack[-n]
        if p_del == head:
            return head.next
        else:
            pre = stack[-n-1]
            pre.next = p_del.next
        return head

head = [1,2,3,4,5]
n = 2
solution = Solution()
print(solution.removeNthFromEnd(head, n))