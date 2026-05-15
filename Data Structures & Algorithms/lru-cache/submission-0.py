class Node:
    def __init__(self, key: Optional[int] = None, val: Optional[int] = None):
        self.key = key
        self.val = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = Node(0, 0) 
        self.end = Node(0, 0)    
        self.start.next = self.end
        self.end.prev = self.start

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev    

    def _insert(self, node: Node): 
        nxt = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            removable = self.end.prev
            self._remove(removable)
            del self.cache[removable.key] 