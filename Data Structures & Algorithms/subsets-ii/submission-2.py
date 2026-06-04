class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(subset, i):            
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                backtrack(subset + [nums[j]], j + 1)

        
        backtrack([], 0)

        return res