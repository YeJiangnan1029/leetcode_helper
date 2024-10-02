from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        pslow, pfast = head, head
        while pfast:
            # 快指针走2步
            pfast = pfast.next
            if pfast is None:
                return None
            pfast = pfast.next
            if pfast is None:
                return None
            # 慢指针走1步
            pslow = pslow.next
            if pslow == pfast:
                break
        new_p = head
        while new_p != pslow:
            new_p = new_p.next
            pslow = pslow.next
        return new_p

head = [3,2,0,-4]
pos = 1
solution = Solution()
print(solution.detectCycle(head, pos))