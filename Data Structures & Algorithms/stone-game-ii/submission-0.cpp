#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// Speed up standard I/O operations
static const int _ = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        const int n = piles.size();
        
        static int dp[105][105];
        static int suffix_sum[105];
        
        suffix_sum[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            suffix_sum[i] = piles[i] + suffix_sum[i + 1];
        }
        
        for (int i = n - 1; i >= 0; --i) {
            for (int M = 1; M <= n; ++M) {
                if (i + 2 * M >= n) {
                    dp[i][M] = suffix_sum[i];
                    continue;
                }
                
                int min_opponent = 1e9;
                int limit = 2 * M;
                
                for (int X = 1; X <= limit; ++X) {
                    int next_val = dp[i + X][M > X ? M : X]; 
                    if (next_val < min_opponent) {
                        min_opponent = next_val;
                    }
                }
                
                dp[i][M] = suffix_sum[i] - min_opponent;
            }
        }
        
        return dp[0][1];
    }
};