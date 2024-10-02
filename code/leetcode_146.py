class LRUCache:
    class ListNode:
        def __init__(self, key, val=-1, next=None, pre=None) -> None:
            self.key = key
            self.val = val
            self.next = next
            self.pre = pre

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = dict()
        self.dummy = LRUCache.ListNode(key="")
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key in self.hash_table:
            # TODO, update key date
            key_node = self.hash_table[key]
            if key_node != self.tail:
                # first delete
                if key_node.next:
                    key_node.next.pre = key_node.pre
                key_node.pre.next = key_node.next
                if key_node == self.tail:
                    self.tail = key_node.pre
                # append at last
                key_node.pre = self.tail
                self.tail.next = key_node
                self.tail = key_node
            return self.hash_table[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.hash_table[key].val = value
            # TODO, update key date
            key_node = self.hash_table[key]
            if key_node != self.tail:
                # first delete
                if key_node.next:
                    key_node.next.pre = key_node.pre
                key_node.pre.next = key_node.next
                if key_node == self.tail:
                    self.tail = key_node.pre
                # append at last
                key_node.pre = self.tail
                self.tail.next = key_node
                self.tail = key_node

        else:
            if len(self.hash_table) >= self.capacity:
                # delete head
                head = self.dummy.next
                if head.next:
                    head.next.pre = self.dummy
                self.dummy.next = head.next
                self.hash_table.pop(head.key)
                if self.tail == head:
                    self.tail = head.pre
                    
            # insert new key
            new_node = LRUCache.ListNode(key, value)
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.hash_table[key] = new_node

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)