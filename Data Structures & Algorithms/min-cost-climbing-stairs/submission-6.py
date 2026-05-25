class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) < 2:
            return 0
            
        two_steps_ahead = cost[-1]
        one_step_ahead = cost[-2]
        
        for i in range(len(cost) - 3, -1, -1):
            current = cost[i] + min(one_step_ahead, two_steps_ahead)
            two_steps_ahead = one_step_ahead
            one_step_ahead = current
            
        return min(one_step_ahead, two_steps_ahead)