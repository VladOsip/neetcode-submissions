class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  
        result = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx
            
            stack.append(idx)

        return result