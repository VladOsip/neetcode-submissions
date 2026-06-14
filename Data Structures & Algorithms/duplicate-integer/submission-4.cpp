class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int,int> checked;
        for (int num : nums){
            if (checked.contains(num)){
                return true;
            }
            checked[num]+=1;
        }
        return false;
    }
};