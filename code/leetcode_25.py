from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        p = head
        while p:
            nums.append(p)
            p = p.next
        it = len(nums) // k
        for i in range(it):
            for j in range(k//2):
                nums[i*k+j], nums[(i+1)*k-1-j] = nums[(i+1)*k-1-j], nums[i*k+j]

        head = nums[0]
        for i in range(len(nums)-1):
            nums[i].next = nums[i+1]
        nums[-1].next = None
        return head

head = [1,2,3,4,5]
k = 2
solution = Solution()
print(solution.reverseKGroup(head, k))