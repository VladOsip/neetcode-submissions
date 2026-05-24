class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, path):
            if idx == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[idx])
            backtrack(idx+1,path)
            path.pop()
            backtrack(idx+1,path)
        backtrack(0,[])

        return result

