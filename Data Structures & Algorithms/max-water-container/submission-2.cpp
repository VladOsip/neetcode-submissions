class Solution {
public:
    int maxArea(std::vector<int>& heights) {
        int total_max = 0;
        int low = 0;
        int high = heights.size() - 1;

        while (low < high) {
            int height = std::min(heights[low], heights[high]);
            int length = high - low;
            total_max = std::max(total_max, height * length);

            if (heights[low] < heights[high]) {
                low++;
            } else {
                high--;
            }
        }

        return total_max;
    }
};