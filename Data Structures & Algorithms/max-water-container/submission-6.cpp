class Solution {
public:
    int maxArea(const std::vector<int>& heights) {
        int max_water = 0;
        int left = 0;
        int right = static_cast<int>(heights.size()) - 1;

        while (left < right) {
            int width = right - left;
            int current_area = 0;

            if (heights[left] < heights[right]) {
                current_area = heights[left] * width;
                ++left;
            } else {
                current_area = heights[right] * width;
                --right;
            }

            if (current_area > max_water) {
                max_water = current_area;
            }
        }

        return max_water;
    }
};