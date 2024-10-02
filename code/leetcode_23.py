from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None and list2 is None:
                return None
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            if list1.val < list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2
        
        while len(lists) > 1:
            temp = []
            for i in range((len(lists)+1)//2):
                if 2*i+1 < len(lists):
                    temp.append(mergeTwoLists(lists[2*i], lists[2*i+1]))
                else:
                    temp.append(lists[2*i])
            lists = temp
        return lists[0]


lists = [[1,4,5],[1,3,4],[2,6]]
solution = Solution()
print(solution.mergeKLists(lists))