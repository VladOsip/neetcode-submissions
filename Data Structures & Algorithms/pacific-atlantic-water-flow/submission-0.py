class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            queue = collections.deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            return visited
        
        pac_starts = []
        atl_starts = []
        
        for r in range(rows):
            pac_starts.append((r, 0))
            atl_starts.append((r, cols - 1))
            
        for c in range(cols):
            pac_starts.append((0, c))
            atl_starts.append((rows - 1, c))
            
        pacific = bfs(pac_starts)
        atlantic = bfs(atl_starts)
        
        return list(pacific.intersection(atlantic))