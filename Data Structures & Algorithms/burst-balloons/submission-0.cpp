class Solution {
public:
    int maxCoins(std::vector<int>& nums) {
        int n = nums.size();
        
        std::vector<int> arr(n + 2, 1);
        for (int i = 0; i < n; ++i) {
            arr[i + 1] = nums[i];
        }
        
        std::vector<std::vector<int>> dp(n + 2, std::vector<int>(n + 2, 0));
        
        for (int window = 1; window <= n; ++window) {
            for (int left = 1; left <= n - window + 1; ++left) {
                int right = left + window - 1;
                
                for (int k = left; k <= right; ++k) {
                    int coins = arr[left - 1] * arr[k] * arr[right + 1];
                    int total = coins + dp[left][k - 1] + dp[k + 1][right];
                    dp[left][right] = std::max(dp[left][right], total);
                }
            }
        }
        
        return dp[1][n];
    }
};
