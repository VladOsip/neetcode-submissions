import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
            
        visited = [False] * n
        total_cost = 0
        edges_used = 0
        
        # Min-heap stores (cost, point_index)
        min_heap = [(0, 0)]
        
        while edges_used < n:
            cost, u = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
                
            visited[u] = True
            total_cost += cost
            edges_used += 1
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
                    
        return total_cost