class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0,0

        for i in range(len(nums)):
            total = max(first+nums[i],second)
            first = second
            second = total
        
        return total
