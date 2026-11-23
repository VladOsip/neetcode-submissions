class Solution {
public:
    int helper(std::span<const int> nums) {
        int first = 0;
        int second = 0;
        for (int num : nums) {
            int total = std::max(first + num, second);
            first = second;
            second = total;
        }
        return second;
    }

    int rob(const std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }

        std::span<const int> view(nums);
        return std::max(
            helper(view.subspan(0, nums.size() - 1)),
            helper(view.subspan(1))
        );
    }
};