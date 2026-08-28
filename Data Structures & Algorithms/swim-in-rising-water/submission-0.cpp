class Solution {
public:
    int swimInWater(std::vector<std::vector<int>>& grid) {
        int n = grid.size();
        // Min-priority queue storing {max_elevation, row, col}
        std::priority_queue<
            std::vector<int>, 
            std::vector<std::vector<int>>, 
            std::greater<std::vector<int>>
        > pq;

        std::vector<std::vector<bool>> visited(n, std::vector<bool>(n, false));
        pq.push({grid[0][0], 0, 0});
        visited[0][0] = true;

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();

            int time = curr[0], r = curr[1], c = curr[2];

            // If we reach the bottom-right corner, return the time
            if (r == n - 1 && c == n - 1) {
                return time;
            }

            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // The time needed is the maximum elevation along the path so far
                    int next_time = std::max(time, grid[nr][nc]);
                    pq.push({next_time, nr, nc});
                }
            }
        }

        return -1;
    }
};