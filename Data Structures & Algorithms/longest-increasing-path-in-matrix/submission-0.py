class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
                
            max_path = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
                    
            memo[(r, c)] = max_path
            return max_path

        return max(dfs(r, c) for r in range(m) for c in range(n))
