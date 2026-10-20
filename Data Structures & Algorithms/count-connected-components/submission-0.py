class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        components = 0
        
        for i in range(n):
            if i not in visited:
                components += 1
                queue = collections.deque([i])
                visited.add(i)
                
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
        return components