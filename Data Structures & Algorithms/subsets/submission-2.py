class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def backtrack(start_idx, current_path):
            output.append(list(current_path))

            for i in range(start_idx, len(nums)):
                current_path.append(nums[i])
                
                backtrack(i + 1, current_path)
                
                current_path.pop()
            
        backtrack(0, [])
        return output