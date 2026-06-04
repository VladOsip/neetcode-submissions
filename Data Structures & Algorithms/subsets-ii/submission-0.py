class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = set() 

        def backtrack(idx, path):
            if idx == len(nums):
                result.add(tuple(path))
                return
            
            path.append(nums[idx])
            backtrack(idx + 1, path)
            path.pop()
            backtrack(idx + 1, path)
            
        backtrack(0, [])
        
        return [list(item) for item in result]
