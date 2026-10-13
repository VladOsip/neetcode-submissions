class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def island_count(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            
            island_count(i, j+1)
            island_count(i, j-1)
            island_count(i+1, j)
            island_count(i-1, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1': 
                    island_count(i, j)
                    count += 1
        
        return count