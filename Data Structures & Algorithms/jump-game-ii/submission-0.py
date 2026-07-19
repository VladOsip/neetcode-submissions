class Solution:
    def jump(self, nums: list[int]) -> int:
        # If the array has 1 element, we are already at the end
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Iterate up to the second-to-last element
        for i in range(len(nums) - 1):
            # Update the furthest index reachable from current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump's range
            if i == current_end:
                jumps += 1            # Make a jump
                current_end = farthest # Update the boundary for the next jump
                
                # Optimization: if we can already reach the last index, stop early
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
