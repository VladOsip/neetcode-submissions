class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());        
        int max_streak = 0; 

        for (const auto& num : nums_set) {
            if (!nums_set.contains(num - 1)) {
                int current_num = num;
                int current_streak = 1;

                while (nums_set.contains(current_num + 1)) {
                    current_num += 1;
                    current_streak += 1;
                }

                max_streak = max(max_streak, current_streak);
            }
        }
        
        return max_streak;
    }
};
