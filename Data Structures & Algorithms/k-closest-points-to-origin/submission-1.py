import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            dist = x**2 + y**2
            
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (dist, [x, y]))
            else:
                if dist < max_heap[0][0]:
                    heapq.heappushpop_max(max_heap, (dist, [x, y]))
                    
        return [point for dist, point in max_heap]