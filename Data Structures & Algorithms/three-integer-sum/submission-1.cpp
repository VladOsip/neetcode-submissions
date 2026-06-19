class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> res;
        
        std::sort(nums.begin(), nums.end());
        
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) {
                break;
            }
            
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int low = i + 1;
            int high = n - 1;
            
            while (low < high) {
                int total = nums[i] + nums[low] + nums[high];
                
                if (total == 0) {
                    res.push_back({nums[i], nums[low], nums[high]});
                    low++;
                    high--;
                    
                    while (low < high && nums[low] == nums[low - 1]) {
                        low++;
                    }
                } 
                else if (total < 0) {
                    low++;
                } 
                else {
                    high--;
                }
            }
        }
        
        return res;
    }
};