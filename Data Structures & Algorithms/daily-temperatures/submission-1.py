class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        
        # Micro-optimization: Localize methods to avoid attribute lookups in the loop
        pop = stack.pop
        append = stack.append
        
        for i in range(n):
            curr_temp = temperatures[i]
            # While stack is not empty and current temp is greater than temp at stack's top index
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_i = pop()
                ans[prev_i] = i - prev_i
            append(i)
            
        return ans