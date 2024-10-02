from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        pslow, pfast = head, head
        while pfast:
            # 快指针走2步
            pfast = pfast.next
            if pfast is None:
                return False
            pfast = pfast.next
            if pfast is None:
                return False
            # 慢指针走1步
            pslow = pslow.next
            if pslow == pfast:
                return True

        

head = [3,2,0,-4]
pos = 1
solution = Solution()
print(solution.hasCycle(head, pos))