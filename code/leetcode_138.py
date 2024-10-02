from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        node_ht = dict()
        while p:
            if p not in node_ht:
                node_ht[id(p)] = Node(p.val, None, None)
            p = p.next
        p = head
        new_head = None
        while p:
            new_node = node_ht[id(p)]
            if p == head:
                new_head = new_node
            new_node.next = node_ht[id(p.next)] if p.next else None
            new_node.random = node_ht[id(p.random)] if p.random else None
            p = p.next
        return new_head
        

head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
solution = Solution()
print(solution.copyRandomList(head))