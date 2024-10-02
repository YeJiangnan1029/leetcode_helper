from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        nums = []
        while p:
            nums.append(p)
            p = p.next
        nums = sorted(nums, key=lambda x: x.val)
        head = nums[0]
        for i in range(len(nums)-1):
            nums[i].next = nums[i+1]
        nums[-1].next = None
        return head


head = [4,2,1,3]
solution = Solution()
print(solution.sortList(head))