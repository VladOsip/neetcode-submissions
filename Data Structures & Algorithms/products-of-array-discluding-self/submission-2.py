class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        # Start from 1: current prefix is (prev num * prev prefix)
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
            
        # Start from n-2: current suffix is (next num * next suffix)
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
            
        # Multiply them together
        return [prefix[i] * suffix[i] for i in range(n)]