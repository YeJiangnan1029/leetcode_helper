from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # # n>=2
        # p, q = head, head.next
        # if p==head:
        #     p.next = q.next
        #     q.next = p
        # else:
        p = head
        node_list = []
        while p:
            node_list.append(p)
            p = p.next
        for i in range(len(node_list)//2):
            node_list[2*i], node_list[2*i+1] = node_list[2*i+1], node_list[2*i]
        head = node_list[0]
        node_list.append(None)
        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        return head

head = [1,2,3,4]
solution = Solution()
print(solution.swapPairs(head))