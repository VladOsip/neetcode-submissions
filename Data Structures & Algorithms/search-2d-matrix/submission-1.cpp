class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();       // Number of rows
        int n = matrix[0].size();    // Number of columns
        
        int low = 0;
        int high = (m * n) - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Map 1D index back to 2D matrix coordinates
            int row = mid / n;
            int col = mid % n;
            
            int mid_val = matrix[row][col];
            
            if (mid_val == target) {
                return true;
            } else if (mid_val < target) {
                low = mid + 1;  // Search the right half
            } else {
                high = mid - 1; // Search the left half
            }
        }
        
        return false;
    }
};