class Solution:
    def findTargetSumWays(self, nums: List[int], s: int) -> int:
        total_sum = sum(nums)
        target = (s + total_sum) // 2
        
        if total_sum < s or (s + total_sum) & 1 or target < 0:
            return 0
            
        return self.subsetSum(nums, target)   

    def subsetSum(self, nums: List[int], s: int) -> int:
        dp = [0] * (s + 1)
        dp[0] = 1
        
        for n in nums:
            for i in range(s, n - 1, -1):
                dp[i] += dp[i - n]
                
        return dp[s]