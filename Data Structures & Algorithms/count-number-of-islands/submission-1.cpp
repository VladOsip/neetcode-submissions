class Solution {
private:
    void dfs(std::vector<std::vector<char>>& grid, int r, int c) {
        int rows = grid.size();
        int cols = grid[0].size();

        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') {
            return;
        }

        grid[r][c] = '0';

        dfs(grid, r - 1, c); // Up
        dfs(grid, r + 1, c); // Down
        dfs(grid, r, c - 1); // Left
        dfs(grid, r, c + 1); // Right
    }

public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }

        int islandCount = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == '1') {
                    islandCount++;
                    dfs(grid, i, j);
                }
            }
        }

        return islandCount;
    }
};