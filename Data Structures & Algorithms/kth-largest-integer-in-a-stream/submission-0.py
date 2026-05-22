import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        # Safely push everything onto our min-heap, maintaining size k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # If the heap exceeds size k, the smallest element is irrelevant
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        return self.heap[0]