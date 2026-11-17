class ListNode:
    def __init__(self, val: int = 0, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = ListNode(value, next_node=self.tail, prev_node=self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        first_node = self.head.next
        self.head.next = first_node.next
        first_node.next.prev = self.head
        
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity