class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> checker;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            if (checker.contains(complement)) { 
                return {checker[complement], i}; 
            }            
            checker[nums[i]] = i;
        } 
        
        return {}; 
    }
};