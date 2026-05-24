class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        down_two = 0
        down_one = 0
        
        for i in range(2, len(cost) + 1):
            current = min(down_one + cost[i - 1], down_two + cost[i - 2])
            
            down_two = down_one
            down_one = current
            
        return down_one