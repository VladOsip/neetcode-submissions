class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        append = q.append
        popleft = q.popleft
        INF = 2147483647

        for r in range(rows):
            row = grid[r]
            for c in range(cols):
                if row[c] == 0:
                    append((r, c))

        while q:
            r, c = popleft()
            next_dist = grid[r][c] + 1
            
            nr = r + 1
            if nr < rows:
                target_row = grid[nr]
                if target_row[c] == INF:
                    target_row[c] = next_dist
                    append((nr, c))

            nr = r - 1
            if nr >= 0:
                target_row = grid[nr]
                if target_row[c] == INF:
                    target_row[c] = next_dist
                    append((nr, c))

            nc = c + 1
            if nc < cols:
                row = grid[r]
                if row[nc] == INF:
                    row[nc] = next_dist
                    append((r, nc))

            nc = c - 1
            if nc >= 0:
                row = grid[r]
                if row[nc] == INF:
                    row[nc] = next_dist
                    append((r, nc))