class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = [-1]
        max_area = 0
        
        for i in range(n):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                if h * w > max_area:
                    max_area = h * w
            stack.append(i)
            
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = n - stack[-1] - 1
            if h * w > max_area:
                max_area = h * w
                
        return max_area