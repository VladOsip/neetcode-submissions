class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        if (nums.empty()) {
            return {{}};
        }

        int first = nums[0];
        std::vector<int> sub_nums(nums.begin() + 1, nums.end());
        std::vector<std::vector<int>> perms = permute(sub_nums);
        std::vector<std::vector<int>> res;

        for (const auto& p : perms) {
            for (size_t i = 0; i <= p.size(); ++i) {
                std::vector<int> p_copy = p;
                p_copy.insert(p_copy.begin() + i, first);
                res.push_back(p_copy);
            }
        }

        return res;
    }
};
