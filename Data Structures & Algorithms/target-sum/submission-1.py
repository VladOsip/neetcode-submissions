from functools import lru_cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i: int, current_sum: int) -> int:
            if i == len(nums):
                return 1 if current_sum == target else 0
            
            add_ways = dp(i + 1, current_sum + nums[i])
            sub_ways = dp(i + 1, current_sum - nums[i])
            
            return add_ways + sub_ways

        return dp(0, 0)