class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total_max = 0

        low, high = 0, len(heights)-1

        while low < high:
            height = min(heights[low],heights[high])
            length = high-low
            total_max = max(total_max,height*length)
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return total_max
