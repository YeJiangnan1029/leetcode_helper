from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if list1 is None and list2 is None:
    #         return None
    #     if list1 is None:
    #         return list2
    #     if list2 is None:
    #         return list1
    #     p, q = list1, list2  # p:[1,2,4] q:[1,3,4]
    #     p_pre = p
    #     q_pre = q
    #     head = list1
    #     while p and q:
    #         if p.val < q.val:
    #             if q_pre != q:
    #                 q_pre.next = p

    #             t = p.next
    #             if head == q:
    #                 head = p
    #             p.next = q
    #             q_pre = p
    #             p = t
    #             p_pre = p
    #         else:
    #             if p_pre != p:
    #                 p_pre.next = q

    #             t = q.next
    #             if head == p:
    #                 head = q
    #             q.next = p
    #             p_pre = q
    #             q = t
    #             q_pre = q
    #     return head

    # 递归写法
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
print(solution.mergeTwoLists(list1, list2))