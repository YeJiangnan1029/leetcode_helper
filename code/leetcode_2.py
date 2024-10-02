from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def my_add_two(l1, l2, jw):
            if not l1 and not l2:
                if jw:
                    return ListNode(val=jw)
                else:
                    return None
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            l3 = ListNode(val=(l1.val+l2.val+jw)%10)
            l3.next = my_add_two(l1.next, l2.next, (l1.val+l2.val+jw)//10)
            return l3
        return my_add_two(l1, l2, 0)


l1 = [2,4,3]
l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))